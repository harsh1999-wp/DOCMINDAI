export default function ChatPage() {
  return (
    <main className="flex flex-1 flex-col items-center justify-center p-6">
      <h2 className="text-xl font-semibold text-gray-800">Chat with your documents</h2>
      <p className="mt-2 text-gray-500">Upload a document to get started.</p>
      <button className="rounded-lg border px- 6 py-4 hover:bg-gray-100">Upload</button>
    </main>
  );
}

