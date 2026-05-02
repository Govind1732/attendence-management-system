import { useRef, useState } from "react";
import Webcam from "react-webcam";
import axios from "axios";

const RegisterUser = () => {
  const webcamRef = useRef(null);

  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");

  const handleRegister = async () => {
    if (!name || !email) {
      setMessage("Enter name and email");
      return;
    }

    const imageSrc = webcamRef.current.getScreenshot();

    if (!imageSrc) {
      setMessage("Camera not ready");
      return;
    }

    const blob = await fetch(imageSrc).then(res => res.blob());

    const formData = new FormData();
    formData.append("name", name);
    formData.append("email", email);
    formData.append("file", blob, "register.jpg");

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/users/register",
        formData
      );

      setMessage(res.data.message || "User registered");
    } catch (err) {
      console.error(err);
      setMessage("Registration failed");
    }
  };

  return (
  <div className="max-w-md mx-auto bg-gray-800 p-6 rounded">
    <h2 className="text-xl mb-4">Register User</h2>

    <input
      className="w-full p-2 mb-3 bg-gray-700 rounded"
      placeholder="Name"
      value={name}
      onChange={(e) => setName(e.target.value)}
    />

    <input
      className="w-full p-2 mb-3 bg-gray-700 rounded"
      placeholder="Email"
      value={email}
      onChange={(e) => setEmail(e.target.value)}
    />

    <Webcam ref={webcamRef} className="rounded mb-3" />

    <button
      className="bg-blue-500 px-4 py-2 rounded w-full"
      onClick={handleRegister}
    >
      Register
    </button>

    <p className="mt-3">{message}</p>
  </div>
);
};

export default RegisterUser;