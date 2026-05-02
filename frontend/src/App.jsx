import { useState } from "react";
import Layout from "./components/Layout";
import RegisterUser from "./components/RegisterUser";
import WebcamCapture from "./components/WebcamCapture";
import Dashboard from "./components/Dashboard";

function App() {
  const [page, setPage] = useState("dashboard");

  const renderPage = () => {
    switch (page) {
      case "register":
        return <RegisterUser />;
      case "attendance":
        return <WebcamCapture />;
      default:
        return <Dashboard />;
    }
  };

  return (
    <Layout setPage={setPage}>
      {renderPage()}
    </Layout>
  );
}

export default App;