import React from "react";
import {
  placeholder,
  codex,
  VIT,
  BHFL,
} from "../assets";

import StackIcon from "tech-stack-icons";
import {
  AiFillMail,
  AiFillLinkedin,
} from "react-icons/ai";

import {
SiJfrogpipelines,
SiOwasp,
SiNx
} from "react-icons/si";

import { FaRegImage, FaRedhat, FaCrown,FaSearchDollar  } from "react-icons/fa";


export const resumeLink = "";
export const callToAction = "https://www.linkedin.com/in/lakshay-baheti/";

export const navLinks = [
  {
    id: "skills",
    title: "Skills & Experience",
  },
  {
    id: "education",
    title: "Education",
  },
  // {
  //   id: "achievements",
  //   title: "Achievements",
  // },
  {
    id: "projects",
    title: "Projects",
  },
  // {
  //   id: "openSource",
  //   title: "Open Source",
  // },
  {
    id: "contactMe",
    title: "Contact Me",
  },
];

// Add your past academic experiences here
export const educationList = [
  {
    id: "education-1",
    icon: VIT,
    title: "Vellore Institute of Technology",
    degree: "Bachelor of Technology - BTech",
    duration: "Jun 2018 - Jun 2022",
    content1: "",
    content2: ""
  }
];

// Add your past achievements here for example - rankings in hackathons/events
export const achievements = [
  {
    id: "a-1",
    icon: FaRegImage,
    event: "",
    position: "",
    content1: "",
    content2: "",
    content3: "",
    article: "",
    project: "",
    youtube: "",
    github: "",
  },
];

// Add your software developments skills here for example - programming languages, frameworks etc.
export const skills = [
  {
    title: "Frameworks/Libraries",
    items: [
      {
        id: "f-1",
icon: (props) => React.createElement(StackIcon, { name: "nextjs", variant: "dark", style: { width: 32, height: 32 }, ...props }),
    name: "Nextjs"
  },
  {
    id: "f-2",
icon: (props) => React.createElement(StackIcon, { name: "react", variant: "dark", style: { width: 32, height: 32 }, ...props }),
    name: "React.js"
  },
  {
    id: "f-3",
    icon: (props) => React.createElement(StackIcon, { name: "react", style: { width: 32, height: 32 }, variant: "dark", ...props }),
    name: "React Native"
  },
  {
    id: "f-4",
icon: (props) => React.createElement(StackIcon, { name: "spring", variant: "dark", style: { width: 32, height: 32 }, ...props }),
    name: "Spring Boot"
  }
    ]
  },
  {
    title: "Tools",
    items: [
      {
        id: "t-1",
        icon: SiNx ,
        name: "nx"
      },
      {
        id: "t-2",
        icon: SiJfrogpipelines,
        name: "Continuous Integration and Continuous Delivery (CI/CD)"
      },
      {
        id: "t-4",
icon: (props) => React.createElement(StackIcon, { name: "typescript", variant: "dark", style: { width: 32, height: 32 }, ...props }),
        name: "TypeScript"
      },
      {
        id: "t-5",
icon: (props) => React.createElement(StackIcon, { name: "js", variant: "dark", style: { width: 32, height: 32 }, ...props }),
        name: "JavaScript"
      },
      {
        id: "t-6",
        icon: FaRedhat,
        name: "Cybersecurity"
      },
      {
        id: "t-7",
        icon: FaCrown,
        name: "Technical Leadership"
      },
      {
        id: "t-8",
        icon: SiOwasp,
        name: "OWASP"
      },
      {
        id: "t-9",
        icon: FaSearchDollar,
        name: "Search Engine Optimization (SEO)"
      },
      {
        id: "t-10",
icon: (props) => React.createElement(StackIcon, { name: "java", variant: "dark", style: { width: 32, height: 32 }, ...props }),
        name: "Java"
      },
      {
        id: "t-11",
icon: (props) => React.createElement(StackIcon, { name: "nodejs", variant: "dark", style: { width: 32, height: 32 }, ...props }),
        name: "Node.js"
      },
      {
        id: "t-12",
icon: (props) => React.createElement(StackIcon, { name: "nestjs", variant: "dark", style: { width: 32, height: 32 }, ...props }),
        name: "NestJS"
      }
    ]
  }
];

// Add your current/past professional work experience here
export const experiences = [
  {
    organisation: "Bajaj Finserv Health",
    logo: BHFL,
    link: "",
    positions: [
      {
        title: "Senior Software Developer",
        duration: "Feb 2025 - Present",
        content: [
          {
            text: "",
            link: ""
          }
        ]
      },
      {
        title: "Software Developer",
        duration: "Aug 2023 - Jan 2025",
        content: [
          {
            text: "",
            link: ""
          }
        ]
      },
      {
        title: "Associate Software Developer",
        duration: "Jul 2022 - Aug 2023",
        content: [
          {
            text: "",
            link: ""
          }
        ]
      },
      {
        title: "Software Development Intern",
        duration: "Jan 2022 - Jun 2022",
        content: [
          {
            text: "",
            link: ""
          }
        ]
      }
    ]
  },
  {
    organisation: "Primera Dental Hub",
    logo: placeholder,
    link: "",
    positions: [
      {
        title: "Software Development Intern",
        duration: "Feb 2021 - Apr 2021",
        content: [
          {
            text: "https://primeradentalhub.",
            link: ""
          },
          {
            text: "com/",
            link: ""
          }
        ]
      }
    ]
  },
  {
    organisation: "Vellore Institute of Technology",
    logo: placeholder,
    link: "",
    positions: [
      {
        title: "Teaching Assistant",
        duration: "Aug 2019 - Aug 2019",
        content: [
          {
            text: "Cybersecurity VAP at VIT  Auriseg and Defsec_1 (Chennai based companies) conducted a value added program on Ethical Hacking in which my role as a teaching assistant was to help setup 150 systems using Active Directory and assist the speakers.",
            link: ""
          }
        ]
      }
    ]
  }
];

// Add information about all the projects to be listed out in your portfolio
export const projects = [
  {
    id: "react-design-pattern",
    title: "React Design Pattern Demo",
    github: "https://github.com/luckyy14/react-design-pattern",
    link: "https://codex.lakshaybaheti.com/",
    image: codex,
    content: "A showcase of advanced React design patterns, including demos for Compound Components, Renderless Components, Prop Getters, State Initializers, and more. Built with Vite and React.",
    stack: [
      {
        id: "icon-react",
        icon: (props) => React.createElement(StackIcon, { name: "react", variant: "dark", style: { width: 24, height: 24 }, ...props }),
        name: "React"
      },
      {
        id: "icon-vite",
        icon: (props) => React.createElement(StackIcon, { name: "vite", variant: "dark", style: { width: 24, height: 24 }, ...props }),
        name: "Vite"
      },
      {
        id: "icon-js",
        icon: (props) => React.createElement(StackIcon, { name: "js", style: { width: 24, height: 24 }, variant: "dark", ...props }),
        name: "JavaScript"
      }
    ],
  }
];

// Add links to blogs here
export const blogPosts = [
  {
    id: "post-1",
    title: "Blog Post 01 - Title",
    link: "#",
    date: new Date().toLocaleDateString(), // Can be edited to any string format
    image: "https://via.placeholder.com/600/92c952",
    tags: [
      {
        id: "tag-1",
        name: "tag 01",
      },
      {
        id: "tag-2",
        name: "tag 03",
      },
      {
        id: "tag-3",
        name: "tag 03",
      },
    ],
  },
];

// Highlight your GitHub stats like - Organisation, Issues Opened, Pull Requests etc.
export const stats = [
  {
    id: "stats-1",
    title: "Organisations",
    value: "2+",
  },
  {
    id: "stats-2",
    title: "Issues Opened",
    value: "6+",
  },
  {
    id: "stats-3",
    title: "Pull Requests",
    value: "6+",
  },
];

// List out the extra curricular activities you have indulged in like - student clubs, joining research groups etc.
export const extraCurricular = [
  {
    id: 1,
    organisation: "",
    title: "",
    duration: "",
    content: [
      {
        text: "",
        link: "",
      },
      {
        text: "",
        link: "",
      },
    ],
    logo: placeholder,
  },
];

// Links to your social media profiles
export const socialMedia = [
  {
    id: "social-media-1",
    icon: AiFillLinkedin,
    link: "https://www.linkedin.com/in/lakshay-baheti/",
  },
  {
    id: "social-media-2",
    icon: (props) => React.createElement(StackIcon, {  name: "github", style: { width: 21, height: 21, display:"block" }, variant: "dark", ...props }),
    link: "https://www.github.com/<your-github-id>/",
  },
  {
    id: "social-media-3",
    icon: AiFillMail,
    link: "mailto:<lakshayb.work@gmail.com>",
  }
];

// Your professional summary
export const aboutMe = {
    name: "Lakshay Baheti",
    githubUsername: "luckyy14",
    tagLine: "Software Developer II@ Bajaj Finserv Health | React.js | Node | SpringBoot",
    intro: "Passionate Frontend Engineer with 3.5+ years of experience building scalable web applications in healthcare SaaS. Proficient in React.js, Next.js, TypeScript, and Nx monorepos, with hands-on experience in Micro Frontend architecture and backend integration using Spring Boot and NestJS."
};

// The maximum number of PRs to be displayed in the Open Source Contributions section.
export const itemsToFetch = 20;

// Add names of GitHub repos you'd like to display open source contributions from in the 'org/repo' format.
export const includedRepos = [
  "publiclab/plots2",
  "zulip/zulip",
  "paritytech/polkadot-sdk",
];
