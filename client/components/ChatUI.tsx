"use client";

import { useChat } from "@/hooks/useChat";
import { useState, FormEvent, useEffect, useRef } from "react";
import { MessageBubble } from "./MessageBubble";
import { FileUpload } from "./FileUpload";
import { motion, AnimatePresence } from "framer-motion";

export const ChatUI = () => {
  const { messages, sendMessage, uploadFiles, loading } = useChat();
  const [input, setInput] = useState("");
  const scrollRef = useRef<HTMLDivElement>(null);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;
    sendMessage(input);
    setInput("");
  };

  // Auto-scroll to the bottom when messages change
  useEffect(() => {
    scrollRef.current?.scrollTo({
      top: scrollRef.current.scrollHeight,
      behavior: "smooth",
    });
  }, [messages]);

  return (
    <motion.div
      className="max-w-2xl mx-auto mt-10 bg-white rounded-2xl shadow-lg overflow-hidden"
      initial={{ opacity: 0, y: 30 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      {/* Top Section - File Upload */}
      <motion.div
        className="p-6 border-b border-gray-200 bg-gray-50 rounded-t-2xl"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.3 }}
      >
        <FileUpload onUpload={uploadFiles} />
      </motion.div>

      {/* Bottom Section - Chat */}
      <div className="flex flex-col p-6 gap-4">
        <motion.div
          ref={scrollRef}
          className="h-[400px] text-slate-700 overflow-y-auto bg-gray-50 p-4 rounded-xl border border-gray-200"
        >
          <AnimatePresence initial={false}>
            {messages.map((msg, idx) => (
              <motion.div
                key={idx}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, y: -20 }}
                transition={{ type: "spring", stiffness: 120, damping: 20 }}
              >
                <MessageBubble type={msg.type} text={msg.text} />
              </motion.div>
            ))}
          </AnimatePresence>

          {loading && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="text-gray-700 italic mt-2"
            >
              Loading...
            </motion.div>
          )}
        </motion.div>

        <motion.form
          onSubmit={handleSubmit}
          className="flex gap-3"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 0.5 }}
        >
          <motion.input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Type your message..."
            className="flex-1 border text-gray-700 border-gray-300 rounded-xl p-3 focus:outline-none focus:ring-2 focus:ring-blue-500"
            whileFocus={{ scale: 1.02 }}
          />
          <motion.button
            type="submit"
            disabled={loading}
            className="bg-blue-600 text-white font-semibold px-5 rounded-xl hover:bg-blue-700 disabled:opacity-50"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            Send
          </motion.button>
        </motion.form>
      </div>
    </motion.div>
  );
};
