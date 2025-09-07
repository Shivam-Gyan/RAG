// utils/api.ts
export const uploadPDFs = async (files: File[]) => {
  const formData = new FormData();
  files.forEach(file => formData.append('files', file));
  const res = await fetch('http://127.0.0.1:8000/upload_pdfs', { method: 'POST', body: formData });
  return res.json();
}

export const sendQuery = async (question: string) => {
  const formData = new FormData();
  formData.append('question', question);
  const res = await fetch('http://127.0.0.1:8000/query', { method: 'POST', body: formData });
  return res.json();
}
