export default function Loading() {
  return (
    <div className="flex items-center justify-center min-h-screen bg-slate-800">
      <div className="p-12 rounded-md shadow-md bg-slate-100">
        <div className="flex flex-col items-center">
          <svg
            className="w-5 text-gray-500 animate-spin h-"
            xmlns="http://www.w3.org/2000/svg"
            fill="none"
            viewBox="0 0 24 24"
          >
            <path
              className="opacity-50"
              fill="currentColor"
              d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3"
            ></path>
          </svg>
        </div>
      </div>
    </div>
  );
}