

const Layout = ({ children, setPage }) => {
  return (
    <div className="flex h-screen bg-gray-900 text-white">

      {/* Sidebar */}
      <div className="w-64 bg-gray-800 p-5">
        <h2 className="text-xl font-bold mb-6">Attendance System</h2>

        <button
          className="block w-full text-left mb-3 hover:text-blue-400"
          onClick={() => setPage("dashboard")}
        >
          Dashboard
        </button>

        <button
          className="block w-full text-left mb-3 hover:text-blue-400"
          onClick={() => setPage("register")}
        >
          Register User
        </button>

        <button
          className="block w-full text-left hover:text-blue-400"
          onClick={() => setPage("attendance")}
        >
          Mark Attendance
        </button>
      </div>

      {/* Main */}
      <div className="flex-1 p-6">
        {children}
      </div>
    </div>
  );
};

export default Layout;