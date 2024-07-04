import React from "react";
import data from "../db.json";
function General() {
  const news = data.generalNews;

  return (
    <div className="flex flex-col items-center justify-center p-4 bg-gray-100 min-h-screen">
      <h1 className="text-4xl font-poppins mb-8">
        Top 10 General News Articles
      </h1>
      <div className="w-full max-w-4xl">
        {news.map((item) => (
          <div
            key={item.id}
            className="my-4 p-4 border rounded shadow bg-white"
          >
            <h2 className="text-2xl font-bold mb-2 text-center">
              {item.title}
            </h2>
            <p className="text-gray-600 mb-2 text-center">By {item.author}</p>
            <p className="text-center">{item.body}</p>
            <div className="text-center mt-2">
              <a
                href={item.link}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-500 underline"
              >
                Read more
              </a>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default General;
