"use client";

import { ChangeEvent, useState } from "react";
import { motion } from "framer-motion";

interface Props {
  onUpload: (files: File[]) => void;
}

export const FileUpload = ({ onUpload }: Props) => {
  const [hovered, setHovered] = useState(false);
  const [selectedFiles, setSelectedFiles] = useState<File[]>([]);

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files) return;
    const filesArray = Array.from(e.target.files);
    setSelectedFiles(filesArray);
    onUpload(filesArray);
  };

  return (
    <motion.label
      htmlFor="file-upload"
      className={`w-full p-6 flex flex-col items-center justify-center border-2 border-dashed rounded-xl cursor-pointer transition-colors ${
        hovered ? "border-blue-500 bg-blue-50" : "border-gray-300 bg-gray-50"
      }`}
      onHoverStart={() => setHovered(true)}
      onHoverEnd={() => setHovered(false)}
      whileTap={{ scale: 0.95 }}
    >
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 0.5 }}
        className="text-center"
      >
        <p className="text-gray-700 font-medium mb-2">
          Drag & Drop files here or click to upload
        </p>
        <p className="text-gray-500 text-sm">
          Only PDFs are allowed. Multiple files supported.
        </p>
      </motion.div>

      <input
        id="file-upload"
        type="file"
        multiple
        accept="application/pdf"
        onChange={handleChange}
        className="hidden"
      />

      {selectedFiles.length > 0 && (
        <motion.ul
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="mt-4 space-y-1 w-full text-gray-800"
        >
          {selectedFiles.map((file, idx) => (
            <motion.li
              key={idx}
              className="p-2 bg-gray-100 rounded flex justify-between items-center"
              initial={{ x: -20, opacity: 0 }}
              animate={{ x: 0, opacity: 1 }}
              transition={{ delay: idx * 0.1 }}
            >
              {file.name}
            </motion.li>
          ))}
        </motion.ul>
      )}
    </motion.label>
  );
};
