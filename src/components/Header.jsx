import React from "react";
import video from "../assets/video.mp4";

function Header() {
  return (
    <header className="relative h-screen flex items-center justify-center overflow-hidden">
      <video
        className="absolute top-0 left-0 w-full h-full object-cover"
        src={video}
        autoPlay
        loop
        muted
      ></video>
      <div className="relative z-10 text-center">
        <h1 className="text-5xl text-white font-bold bg-black bg-opacity-50 p-4 rounded">
          Welcome to the ASX 100 Newsletter!
        </h1>
        <p className="mt-4 text-lg text-white bg-black bg-opacity-50 p-4 rounded max-w-xl mx-auto">
          This is a newsletter designed to help you stay up-to-date with the
          latest ASX 100 news. We desire to help beginners, passive, and active
          investors to seek optimal investments. Catering to your needs and
          interests is what keeps your money a float, and we are here to help.
        </p>
      </div>
      <div className="absolute inset-0 bg-black opacity-50"></div>
    </header>
  );
}

export default Header;
