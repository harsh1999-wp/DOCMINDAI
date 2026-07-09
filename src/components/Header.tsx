export default function Header() {
  return (
    <header className="flex h-16 items-center justify-between border-b bg-white px-6">
      <h1 className="text-2xl font-bold text-blue-600">DocMind AI</h1>

      <button className="rounded-lg border px- 6 py-4 hover:bg-gray-100">Setting</button>
    </header>
  );
}