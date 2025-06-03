import os
import csv
import re
import json
import argparse
from datetime import datetime


def get_default_paths():
    """Get default paths for input and output files"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return {
        'input_dir': os.path.join(script_dir, "linkedin-export"),
        'output': os.path.join(script_dir, "..", "src", "constants", "index-example.js"),
        'json_output': os.path.join(script_dir, "constants.json")
    }


def parse_date(date_str):
    """Parse date string in format 'MMM YYYY' to datetime object"""
    if not date_str:
        return None
    try:
        return datetime.strptime(date_str.strip(), '%b %Y')
    except ValueError:
        return None


def format_date(date_str):
    """Format date string to 'MMM YYYY' format"""
    if not date_str:
        return ""
    try:
        date = parse_date(date_str)
        return date.strftime('%b %Y')
    except (ValueError, TypeError):
        return date_str


def convert_education_csv_to_js(input_dir=None, output_file=None):
    # Define paths
    if input_dir is None or output_file is None:
        paths = get_default_paths()
        input_dir = input_dir or paths['input_dir']
        output_file = output_file or paths['output']

    input_file = os.path.join(input_dir, "Education.csv")
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        return False

    # Read education data from CSV
    education_entries = []
    try:
        with open(input_file, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                # Extract data
                school_name = row.get("School Name", "").strip()
                start_date = row.get("Start Date", "").strip()
                end_date = row.get("End Date", "").strip()
                notes = row.get("Notes", "").strip()
                degree_name = row.get("Degree Name", "").strip()
                activities = row.get("Activities", "").strip()

                # Format duration
                duration = ""
                if start_date and end_date:
                    duration = f"{start_date} - {end_date}"
                elif start_date:
                    duration = f"{start_date} - Present"

                # Create entry
                entry = {
                    "id": f"education-{i + 1}",
                    "icon": "FaRegImage",
                    "title": school_name,
                    "degree": degree_name,
                    "duration": duration,
                    "content1": notes,
                    "content2": activities,
                }

                education_entries.append(entry)

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False

    # Generate JS code for education list
    js_entries = []
    for entry in education_entries:
        template = '''  {
    id: "%s",
    icon: %s,
    title: "%s",
    degree: "%s",
    duration: "%s",
    content1: "%s",
    content2: "%s"
  }'''
        js_entry = template % (
            entry["id"],
            entry["icon"],
            entry["title"],
            entry["degree"],
            entry["duration"],
            entry["content1"],
            entry["content2"]
        )
        js_entries.append(js_entry)

    js_code = "export const educationList = [\n" + ",\n".join(js_entries) + "\n];\n"

    # Check if output file exists and contains relevant section
    try:
        content = ""
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Check if educationList is already defined
            if "export const educationList" in content:
                # Replace existing educationList
                pattern = r"export const educationList = \[[\s\S]*?\];"
                content = re.sub(pattern, js_code.strip(), content)
            else:
                # Append educationList to the end
                content += "\n\n" + js_code
        else:
            # Create new file with educationList
            content = js_code

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write updated content to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully updated {output_file} with education data.")
        return education_entries

    except Exception as e:
        print(f"Error updating JS file: {e}")
        return False


def convert_projects_csv_to_js(input_dir=None, output_file=None):
    # Define paths
    if input_dir is None or output_file is None:
        paths = get_default_paths()
        input_dir = input_dir or paths['input_dir']
        output_file = output_file or paths['output']

    input_file = os.path.join(input_dir, "Projects.csv")
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        return False

    # Read projects data from CSV
    project_entries = []
    try:
        with open(input_file, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                # Extract data
                title = row.get("Title", "").strip()
                description = row.get("Description", "").strip()
                url = row.get("Url", "").strip()
                # started_on = row.get("Started On", "").strip()
                # finished_on = row.get("Finished On", "").strip()

                # Create entry
                entry = {
                    "id": f"project-{i + 1}",
                    "title": title,
                    "github": url,
                    "link": url,
                    "image": "placeholder",
                    "content": description,
                    "stack": [
                        {
                            "id": "icon-1",
                            "icon": "FaRegImage",
                            "name": "Placeholder",
                        }
                    ],
                }

                project_entries.append(entry)

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False

    # Generate JS code for projects list
    js_entries = []
    for entry in project_entries:
        # Format stack items
        stack_items = []
        for stack in entry["stack"]:
            stack_template = '''      {
            id: "%s",
            icon: %s,
            name: "%s"
        }'''
            stack_item = stack_template % (
                stack["id"],
                stack["icon"],
                stack["name"]
            )
            stack_items.append(stack_item)

        stack_items_str = ",\n".join(stack_items)  # Precompute the string here

        template = '''  {
        id: "%s",
        title: "%s",
        github: "%s",
        link: "%s",
        image: %s,
        content: "%s",
        stack: [
    %s
        ]
    }'''
        js_entry = template % (
            entry["id"],
            entry["title"],
            entry["github"],
            entry["link"],
            entry["image"],
            entry["content"],
            stack_items_str
        )
        js_entries.append(js_entry)

    js_code = "export const projects = [\n" + ",\n".join(js_entries) + "\n];\n"


    # Check if output file exists and contains relevant section
    try:
        content = ""
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Check if projects is already defined
            if "export const projects" in content:
                # Replace existing projects
                pattern = r"export const projects = \[[\s\S]*?\];"
                content = re.sub(pattern, js_code.strip(), content)
            else:
                # Append projects to the end
                content += "\n\n" + js_code
        else:
            # Create new file with projects
            content = js_code

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write updated content to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully updated {output_file} with projects data.")
        return project_entries

    except Exception as e:
        print(f"Error updating JS file: {e}")
        return False


def convert_volunteering_csv_to_js(input_dir=None, output_file=None):
    # Define paths
    if input_dir is None or output_file is None:
        paths = get_default_paths()
        input_dir = input_dir or paths['input_dir']
        output_file = output_file or paths['output']

    input_file = os.path.join(input_dir, "Volunteering.csv")
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        return False

    # Read volunteering data from CSV
    volunteering_entries = []
    try:
        with open(input_file, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                # Extract data
                company_name = row.get("Company Name", "").strip()
                role = row.get("Role", "").strip()
                started_on = row.get("Started On", "").strip()
                finished_on = row.get("Finished On", "").strip()
                description = row.get("Description", "").strip()

                # Format duration
                duration = ""
                if started_on and finished_on:
                    duration = f"{started_on} - {finished_on}"
                elif started_on:
                    duration = f"{started_on} - Present"

                # Split description by periods to create content items
                content_items = []
                if description:
                    # Split by period but keep the period in the text
                    sentences = [
                        s.strip() + "." for s in description.split(".") if s.strip()
                    ]
                    # Remove the last period if the original text didn't end with a period
                    if not description.endswith(".") and sentences:
                        sentences[-1] = sentences[-1][:-1]

                    for sentence in sentences:
                        if sentence.strip():
                            content_items.append({"text": sentence.strip(), "link": ""})

                # If no content items were created, add an empty one
                if not content_items:
                    content_items.append({"text": "", "link": ""})

                # Create entry
                entry = {
                    "id": i + 1,
                    "organisation": company_name,
                    "title": role,
                    "duration": duration,
                    "content": content_items,
                    "logo": "placeholder",
                }

                volunteering_entries.append(entry)

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False

    # Generate JS code for extraCurricular list
    js_entries = []
    for entry in volunteering_entries:
        # Format content items
        content_items = []
        for content in entry["content"]:
            template = '''      {
        text: "%s",
        link: "%s"
      }'''
            content_item = template % (content["text"], content["link"])
            content_items.append(content_item)

        template = '''  {
    id: %s,
    organisation: "%s",
    title: "%s",
    duration: "%s",
    content: [
%s
    ],
    logo: %s
  }'''
        js_entry = template % (
            entry["id"],
            entry["organisation"],
            entry["title"],
            entry["duration"],
            ",\n".join(content_items),
            entry["logo"]
        )
        js_entries.append(js_entry)

    js_code = "export const extraCurricular = [\n" + ",\n".join(js_entries) + "\n];\n"

    # Check if output file exists and contains relevant section
    try:
        content = ""
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Check if extraCurricular is already defined
            if "export const extraCurricular" in content:
                # Replace existing extraCurricular
                pattern = r"export const extraCurricular = \[[\s\S]*?\];"
                content = re.sub(pattern, js_code.strip(), content)
            else:
                # Append extraCurricular to the end
                content += "\n\n" + js_code
        else:
            # Create new file with extraCurricular
            content = js_code

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write updated content to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully updated {output_file} with volunteering data.")
        return volunteering_entries

    except Exception as e:
        print(f"Error updating JS file: {e}")
        return False


def convert_honors_csv_to_js(input_dir=None, output_file=None):
    # Define paths
    if input_dir is None or output_file is None:
        paths = get_default_paths()
        input_dir = input_dir or paths['input_dir']
        output_file = output_file or paths['output']

    input_file = os.path.join(input_dir, "Honors.csv")
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        return False

    # Read honors data from CSV
    honors_entries = []
    try:
        with open(input_file, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for i, row in enumerate(reader):
                # Extract data
                title = row.get("Title", "").strip()
                description = row.get("Description", "").strip()
                issued_on = row.get("Issued On", "").strip()

                # Split description by periods for content fields
                if description:
                    # Split by period but keep the period in the text
                    sentences = [
                        s.strip() + "." for s in description.split(".") if s.strip()
                    ]
                    # Remove the last period if the original text didn't end with a period
                    if not description.endswith(".") and sentences:
                        sentences[-1] = sentences[-1][:-1]

                    # First 2 sentences go to content1 and content2
                    content1 = sentences[0] if len(sentences) > 0 else ""
                    content2 = sentences[1] if len(sentences) > 1 else ""
                    # All remaining sentences go to content3
                    content3 = ""
                    if len(sentences) > 2:
                        content3 = " ".join(sentences[2:])
                else:
                    content1 = ""
                    content2 = ""
                    content3 = ""

                # Create entry
                entry = {
                    "id": f"a-{i + 1}",
                    "icon": "FaRegImage",
                    "event": title,
                    "position": issued_on,
                    "content1": content1,
                    "content2": content2,
                    "content3": content3,
                    "article": "",
                    "project": "",
                    "youtube": "",
                    "github": "",
                }

                honors_entries.append(entry)

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False

    # Generate JS code for achievements list
    js_entries = []
    for entry in honors_entries:
        template = '''  {
    id: "%s",
    icon: %s,
    event: "%s",
    position: "%s",
    content1: "%s",
    content2: "%s",
    content3: "%s",
    article: "%s",
    project: "%s",
    youtube: "%s",
    github: "%s"
  }'''
        js_entry = template % (
            entry["id"],
            entry["icon"],
            entry["event"],
            entry["position"],
            entry["content1"],
            entry["content2"],
            entry["content3"],
            entry["article"],
            entry["project"],
            entry["youtube"],
            entry["github"]
        )
        js_entries.append(js_entry)

    js_code = "export const achievements = [\n" + ",\n".join(js_entries) + "\n];\n"

    # Check if output file exists and contains relevant section
    try:
        content = ""
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Check if achievements is already defined
            if "export const achievements" in content:
                # Replace existing achievements
                pattern = r"export const achievements = \[[\s\S]*?\];"
                content = re.sub(pattern, js_code.strip(), content)
            else:
                # Append achievements to the end
                content += "\n\n" + js_code
        else:
            # Create new file with achievements
            content = js_code

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write updated content to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully updated {output_file} with honors data.")
        return honors_entries

    except Exception as e:
        print(f"Error updating JS file: {e}")
        return False


def convert_positions_csv_to_js(input_dir=None, output_file=None):
    # Define paths
    if input_dir is None or output_file is None:
        paths = get_default_paths()
        input_dir = input_dir or paths['input_dir']
        output_file = output_file or paths['output']

    input_file = os.path.join(input_dir, "Positions.csv")
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        return False

    # Read positions data from CSV
    positions_data = []
    try:
        with open(input_file, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                positions_data.append(row)

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False

    # Group positions by organization
    organizations = {}
    for position in positions_data:
        company_name = position.get("Company Name", "").strip()

        if company_name not in organizations:
            organizations[company_name] = []

        organizations[company_name].append(position)

    # Process each organization and its positions
    experience_entries = []
    for company_name, positions in organizations.items():
        # Create organization entry
        org_entry = {
            "organisation": company_name,
            "logo": "placeholder",
            "link": "",
            "positions": [],
        }

        # Sort positions by date (most recent first)
        def get_position_date(position):
            started_on = parse_date(position.get("Started On", "").strip())
            finished_on = parse_date(position.get("Finished On", "").strip())
            # If no end date, use a far future date to sort "Present" positions first
            if not finished_on:
                finished_on = datetime(9999, 12, 31)
            return (started_on, finished_on) if started_on else (datetime.min, datetime.min)

        positions.sort(key=get_position_date, reverse=True)

        # Process each position for this organization
        for position in positions:
            title = position.get("Title", "").strip()
            started_on = position.get("Started On", "").strip()
            finished_on = position.get("Finished On", "").strip()
            description = position.get("Description", "").strip()

            # Format duration
            duration = ""
            if started_on and finished_on:
                duration = f"{format_date(started_on)} - {format_date(finished_on)}"
            elif started_on:
                duration = f"{format_date(started_on)} - Present"

            # Split description into content items
            content_items = []

            # Check if description contains bullet points
            if "•" in description:
                # Split by bullet points
                bullet_items = [
                    item.strip() for item in description.split("•") if item.strip()
                ]
                for item in bullet_items:
                    content_items.append({"text": item, "link": ""})
            else:
                # Split by periods
                sentences = [
                    s.strip() + "." for s in description.split(".") if s.strip()
                ]
                # Remove the last period if the original text didn't end with a period
                if not description.endswith(".") and sentences:
                    sentences[-1] = sentences[-1][:-1]

                for sentence in sentences:
                    if sentence.strip():
                        content_items.append({"text": sentence.strip(), "link": ""})

            # If no content items were created, add a default one with the description
            if not content_items and description:
                content_items.append({"text": description, "link": ""})
            elif not content_items:
                content_items.append({"text": "", "link": ""})

            # Create position entry
            position_entry = {
                "title": title,
                "duration": duration,
                "content": content_items,
            }

            org_entry["positions"].append(position_entry)

        experience_entries.append(org_entry)

    # Generate JS code for experiences list
    js_entries = []
    for entry in experience_entries:
        # Format positions
        positions_items = []
        for position in entry["positions"]:
            # Format content items
            content_items = []
            for content in position["content"]:
                content_template = '''          {
            text: "%s",
            link: "%s"
          }'''
                content_item = content_template % (
                    content["text"],
                    content["link"]
                )
                content_items.append(content_item)

            position_template = '''      {
        title: "%s",
        duration: "%s",
        content: [
%s
        ]
      }'''
            position_item = position_template % (
                position["title"],
                position["duration"],
                ",\n".join(content_items)
            )
            positions_items.append(position_item)

        template = '''  {
    organisation: "%s",
    logo: %s,
    link: "%s",
    positions: [
%s
    ]
  }'''
        js_entry = template % (
            entry["organisation"],
            entry["logo"],
            entry["link"],
            ",\n".join(positions_items)
        )
        js_entries.append(js_entry)

    js_code = "export const experiences = [\n" + ",\n".join(js_entries) + "\n];\n"

    # Check if output file exists and contains relevant section
    try:
        content = ""
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Check if experiences is already defined
            if "export const experiences" in content:
                # Replace existing experiences
                pattern = r"export const experiences = \[[\s\S]*?\];"
                content = re.sub(pattern, js_code.strip(), content)
            else:
                # Append experiences to the end
                content += "\n\n" + js_code
        else:
            # Create new file with experiences
            content = js_code

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write updated content to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully updated {output_file} with positions data.")
        return experience_entries

    except Exception as e:
        print(f"Error updating JS file: {e}")
        return False


def convert_profile_csv_to_js(input_dir=None, output_file=None):
    # Define paths
    if input_dir is None or output_file is None:
        paths = get_default_paths()
        input_dir = input_dir or paths['input_dir']
        output_file = output_file or paths['output']

    input_file = os.path.join(input_dir, "Profile.csv")
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        return False

    # Default values
    name = ""
    githubUsername = ""
    tagLine = ""
    intro = "This is a placeholder intro"

    # Read profile data from CSV
    try:
        with open(input_file, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Only process the first row
                first_name = row.get("First Name", "").strip()
                last_name = row.get("Last Name", "").strip()
                headline = row.get("Headline", "").strip()

                # Format full name
                name = f"{first_name} {last_name}".strip()

                # Use headline as tagLine
                tagLine = headline

                # Only process the first row
                break

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False

    # Generate JS code for aboutMe object
    template = '''export const aboutMe = {
    name: "%s",
    githubUsername: "%s",
    tagLine: "%s",
    intro: "%s"
};'''
    js_code = template % (
        name,
        githubUsername,
        tagLine,
        intro
    )

    # Check if output file exists and contains relevant section
    try:
        content = ""
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Check if aboutMe is already defined
            if "export const aboutMe" in content:
                # Replace existing aboutMe
                pattern = r"export const aboutMe = \{[\s\S]*?\};"
                content = re.sub(pattern, js_code.strip(), content)
            else:
                # Append aboutMe to the end
                content += "\n\n" + js_code
        else:
            # Create new file with aboutMe
            content = js_code

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write updated content to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully updated {output_file} with profile data.")
        return {
            "name": name,
            "githubUsername": githubUsername,
            "tagLine": tagLine,
            "intro": intro
        }

    except Exception as e:
        print(f"Error updating JS file: {e}")
        return False


def convert_skills_csv_to_js(input_dir=None, output_file=None):
    # Define paths
    if input_dir is None or output_file is None:
        paths = get_default_paths()
        input_dir = input_dir or paths['input_dir']
        output_file = output_file or paths['output']

    input_file = os.path.join(input_dir, "Skills.csv")
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Error: Input file {input_file} not found.")
        return False

    common_frameworks = ["flask", "django", "react", "angular", "vue", "laravel", "spring", "bootstrap", "tailwind css", "tailwindcss", "express", "dotnet", "tensorflow", "pytorch", "rubyonrails", "rails", "bootstrap", "jquery", "nodejs", "nextjs", "nuxtjs", "angularjs", "vuejs"]

    # Initialize categories
    programming_languages = []
    frameworks = []
    tools = []

    # Read skills data from CSV
    try:
        with open(input_file, "r", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            pl_count = 1  # Counter for programming languages
            f_count = 1   # Counter for frameworks
            t_count = 1   # Counter for tools

            for row in reader:
                skill_name = row.get("Name", "").strip()

                if not skill_name:
                    continue

                # Check if it's a programming language
                if "(Programming Language)" in skill_name:
                    # Extract the language name without the "(Programming Language)" part
                    language_name = skill_name.replace("(Programming Language)", "").strip()
                    # Generate icon name based on language
                    icon_name = f"Si{language_name.replace(' ', '')}"

                    programming_languages.append({
                        "id": f"pl-{pl_count}",
                        "icon": icon_name,
                        "name": language_name
                    })
                    pl_count += 1

                # Check for common frameworks keywords
                elif any(keyword in skill_name.lower() for keyword in common_frameworks):
                    # Use FaRegImage as a placeholder for framework icons
                    frameworks.append({
                        "id": f"f-{f_count}",
                        "icon": f"Si{skill_name.replace(' ', '').capitalize()}",
                        "name": skill_name
                    })
                    f_count += 1

                # Everything else goes to tools
                else:
                    tools.append({
                        "id": f"t-{t_count}",
                        "icon": "FaRegImage",
                        "name": skill_name
                    })
                    t_count += 1

    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return False

    # Generate skills categories
    categories = []

    # Add programming languages category if not empty
    if programming_languages:
        categories.append({
            "title": "Programming Languages",
            "items": programming_languages
        })

    # Add frameworks category if not empty
    if frameworks:
        categories.append({
            "title": "Frameworks/Libraries",
            "items": frameworks
        })

    # Add tools category if not empty
    if tools:
        categories.append({
            "title": "Tools",
            "items": tools
        })

    # Generate JS code for skills list
    js_entries = []
    for category in categories:
        # Format items
        items_entries = []
        for item in category["items"]:
            item_template = '''      {
        id: "%s",
        icon: %s,
        name: "%s"
      }'''
            item_entry = item_template % (
                item["id"],
                item["icon"],
                item["name"]
            )
            items_entries.append(item_entry)

        template = '''  {
    title: "%s",
    items: [
%s
    ]
  }'''
        js_entry = template % (
            category["title"],
            ",\n".join(items_entries)
        )
        js_entries.append(js_entry)

    js_code = "export const skills = [\n" + ",\n".join(js_entries) + "\n];\n"

    # Check if output file exists and contains relevant section
    try:
        content = ""
        if os.path.exists(output_file):
            with open(output_file, "r", encoding="utf-8") as f:
                content = f.read()

            # Check if skills is already defined
            if "export const skills" in content:
                # Replace existing skills
                pattern = r"export const skills = \[[\s\S]*?\];"
                content = re.sub(pattern, js_code.strip(), content)
            else:
                # Append skills to the end
                content += "\n\n" + js_code
        else:
            # Create new file with skills
            content = js_code

            # Create directory if it doesn't exist
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

        # Write updated content to file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(content)

        print(f"Successfully updated {output_file} with skills data.")
        return categories

    except Exception as e:
        print(f"Error updating JS file: {e}")
        return False


def update_json_file(education_entries=None, project_entries=None, volunteering_entries=None, 
                    honors_entries=None, experience_entries=None, profile_data=None, 
                    skills_categories=None, json_file=None):
    """Write all entries to a JSON file while preserving existing data"""
    
    if json_file is None:
        json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "constants.json")

    # Load existing JSON data or create new
    json_data = {}
    if os.path.exists(json_file):
        with open(json_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)

    # Update with new data if provided
    if education_entries is not None:
        json_data['educationList'] = education_entries
    
    if project_entries is not None:
        json_data['projects'] = project_entries
    
    if volunteering_entries is not None:
        json_data['extraCurricular'] = volunteering_entries
    
    if honors_entries is not None:
        json_data['achievements'] = honors_entries
    
    if experience_entries is not None:
        json_data['experiences'] = experience_entries
    
    if profile_data is not None:
        json_data['aboutMe'] = profile_data
    
    if skills_categories is not None:
        json_data['skills'] = skills_categories

    # Ensure essential sections exist with default values
    defaults = {
        'resumeLink': json_data.get('resumeLink', ""),
        'callToAction': json_data.get('callToAction', "https://www.linkedin.com/in/<your-linkedin-id>/"),
        'navLinks': json_data.get('navLinks', [
            {"id": "skills", "title": "Skills & Experience"},
            {"id": "education", "title": "Education"},
            {"id": "achievements", "title": "Achievements"},
            {"id": "projects", "title": "Projects"},
            {"id": "openSource", "title": "Open Source"},
            {"id": "extraCurricular", "title": "Extra Curricular"},
            {"id": "contactMe", "title": "Contact Me"}
        ]),
        'itemsToFetch': json_data.get('itemsToFetch', 20),
        'includedRepos': json_data.get('includedRepos', [
            "publiclab/plots2",
            "zulip/zulip",
            "paritytech/polkadot-sdk"
        ])
    }
    
    # Update json_data with defaults
    json_data.update(defaults)

    # Write updated data to file
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(json_data, f, indent=4)
        
    print(f"Successfully updated {json_file}")

def main():
    parser = argparse.ArgumentParser(description='Convert LinkedIn export CSV files to JS format')
    
    # Add arguments for input directory and output file
    parser.add_argument('--input-dir', help='Directory containing LinkedIn export CSV files')
    parser.add_argument('--output', help='Path to output JS file')
    parser.add_argument('--json-output', help='Path to output JSON file')
    
    args = parser.parse_args()
    
    # Get default paths
    paths = get_default_paths()
    
    input_dir = args.input_dir or paths['input_dir']
    output_file = args.output or paths['output']
    json_file = getattr(args, 'json_output', None) or paths.get('json_output')
    
    # Create variables to store data
    education_data = []
    project_data = []
    volunteering_data = []
    honors_data = []
    experience_data = []
    profile_data = {}
    skills_data = []
    
    # Convert CSV files to data structures
    education_data = convert_education_csv_to_js(input_dir, output_file)
    project_data = convert_projects_csv_to_js(input_dir, output_file)
    volunteering_data = convert_volunteering_csv_to_js(input_dir, output_file)
    honors_data = convert_honors_csv_to_js(input_dir, output_file)
    experience_data = convert_positions_csv_to_js(input_dir, output_file)
    profile_data = convert_profile_csv_to_js(input_dir, output_file)
    skills_data = convert_skills_csv_to_js(input_dir, output_file)
    
    # Update JSON file with all data
    update_json_file(
        education_entries=education_data,
        project_entries=project_data,
        volunteering_entries=volunteering_data,
        honors_entries=honors_data,
        experience_entries=experience_data,
        profile_data=profile_data,
        skills_categories=skills_data,
        json_file=json_file
    )


if __name__ == "__main__":
    main()
