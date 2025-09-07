import { useState } from "react";
import { sendQuery, uploadPDFs } from "@/utils/api";

export interface Message {
  type: "user" | "bot";
  text: string;
}

export const useChat = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [loading, setLoading] = useState(false);

  const sendMessage = async (text: string) => {
    setMessages((prev) => [...prev, { type: "user", text }]);
    setLoading(true);

    try {
      const res = await sendQuery(text);
      setMessages((prev) => [...prev, { type: "bot", text: res.response }]);
    } catch (err) {
      setMessages((prev) => [...prev, { type: "bot", text: "Error getting response" }]);
    } finally {
      setLoading(false);
    }
  };

  const uploadFiles = async (files: File[]) => {
    setLoading(true);
    try {
      const res = await uploadPDFs(files);
      setMessages((prev) => [...prev, { type: "bot", text: res.message || "Files uploaded" }]);
    } catch (err) {
      setMessages((prev) => [...prev, { type: "bot", text: "File upload failed" }]);
    } finally {
      setLoading(false);
    }
  };

  return { messages, sendMessage, uploadFiles, loading };
};
