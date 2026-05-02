import { useRef, useState } from "react";
import Webcam from "react-webcam";
import axios from "axios";

const WebcamCapture = () => {
  const webcamRef = useRef(null);
  const [result, setResult] = useState("");

  const captureAndSend = async () => {
    const imageSrc = webcamRef.current.getScreenshot();

    // Convert base64 → blob
    const blob = await fetch(imageSrc).then(res => res.blob());

    const formData = new FormData();
    formData.append("file", blob, "capture.jpg");

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/attendance/recognize",
        formData
      );

      setResult(res.data.message + " - " + (res.data.user || ""));
    } catch (err) {
      console.error(err);
      setResult("Error occurred");
    }
  };

  return (
  <div className="max-w-md mx-auto bg-gray-800 p-6 rounded text-center">
    <h2 className="text-xl mb-4">Mark Attendance</h2>

    <Webcam ref={webcamRef} className="rounded mb-4" />

    <button
      className="bg-green-500 px-4 py-2 rounded"
      onClick={captureAndSend}
    >
      Mark Attendance
    </button>

    <p className="mt-3 text-lg">{result}</p>
  </div>
);
};

export default WebcamCapture;