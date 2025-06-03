import { motion } from "framer-motion";
import { aboutMe } from "../constants";

const Logo = () => {
  return (
    <motion.a 
      href="#home" 
      className="flex items-center"
      whileHover={{ scale: 1.05 }}
      transition={{ type: "spring", stiffness: 300, damping: 15 }}
    >
      <div className="logo relative flex items-center group">
        <motion.span 
          className="text-[#00f7ff] text-3xl font-bold mr-2"
          initial={false}
          animate={{ x: 0 }}
          whileHover={{ x: -4 }}
        >
          {'{'}
        </motion.span>
        <div className="text-white text-center font-bold leading-tight">
          <motion.span 
            className="text-lg block"
            whileHover={{ color: "rgb(153 246 228)" }}
          >
            {aboutMe.name.split(' ')[0]}
          </motion.span>
          <motion.span 
            className="text-lg block"
            whileHover={{ color: "rgb(153 246 228)" }}
          >
            {aboutMe.name.split(' ')[1]}
          </motion.span>
        </div>
        <motion.span 
          className="text-[#00f7ff] text-3xl font-bold ml-2"
          initial={false}
          animate={{ x: 0 }}
          whileHover={{ x: 4 }}
        >
          {'}'}
        </motion.span>
      </div>
    </motion.a>
  );
};

export default Logo;
