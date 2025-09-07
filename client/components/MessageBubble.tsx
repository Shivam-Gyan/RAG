"use client";

import { motion } from "framer-motion";

interface Props {
  type: "user" | "bot";
  text: string;
}

export const MessageBubble = ({ type, text }: Props) => {
  const isUser = type === "user";

  return (
    <motion.div
      className={`flex ${isUser ? "justify-end" : "justify-start"} mb-2`}
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ type: "spring", stiffness: 120, damping: 20 }}
      whileHover={{ scale: 1.03 }}
    >
      <motion.div
        className={`p-3 rounded-xl max-w-xs break-words ${
          isUser ? "bg-blue-500 text-white" : "bg-gray-200 text-black"
        }`}
        initial={{ scale: 0.8 }}
        animate={{ scale: 1 }}
        transition={{ duration: 0.2 }}
      >
        {text}
      </motion.div>
    </motion.div>
  );
};
