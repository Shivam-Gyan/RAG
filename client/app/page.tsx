"use client";

import { ChatUI } from "@/components/ChatUI";
import { motion } from "framer-motion";

export default function Page() {
  return (
    <main className="min-h-screen bg-gray-100">
      {/* Navbar */}
      <motion.nav
        className="w-full bg-white shadow-md rounded-b-2xl px-6 py-4 flex justify-around items-center"
        initial={{ opacity: 0, y: -50 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, ease: "easeOut" }}
      >
        <div className="flex items-center gap-2 mb-2">
          {/* Logo */}
          <div className="w-10 h-10 bg-blue-600 rounded-full flex items-center justify-center text-white font-bold text-lg">
            M
          </div>
          <span className="text-xl font-semibold text-slate-900">MediBot</span>
        </div>

        {/* Navbar Actions */}
        <div className="flex items-center gap-4">
          <button onClick={() => {alert("Login clicked");}} className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition">
            Login
          </button>
          <button onClick={() => {alert("Help clicked");}} className="px-4 py-2 border text-slate-600 border-gray-300 rounded-lg hover:bg-gray-100 transition">
            Help
          </button>
        </div>
      </motion.nav>

      {/* Page Content */}
      <motion.div
        className="p-4 max-w-3xl mx-auto"
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay: 0.3, ease: "easeOut" }}
      >
        {/* <h1 className="text-2xl font-bold mb-4 text-slate-900 text-center">
          MediBot Chat
        </h1> */}
        <ChatUI />
      </motion.div>
    </main>
  );
}
