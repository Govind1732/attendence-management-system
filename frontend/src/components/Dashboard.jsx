const Dashboard = () => {
  return (
    <div>
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>

      <div className="grid grid-cols-3 gap-4">
        <div className="bg-gray-800 p-5 rounded">
          <h2>Total Users</h2>
          <p className="text-2xl font-bold">--</p>
        </div>

        <div className="bg-gray-800 p-5 rounded">
          <h2>Today Attendance</h2>
          <p className="text-2xl font-bold">--</p>
        </div>

        <div className="bg-gray-800 p-5 rounded">
          <h2>Status</h2>
          <p className="text-green-400">System Active</p>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;