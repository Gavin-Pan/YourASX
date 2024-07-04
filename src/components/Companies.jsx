import React from "react";
import data from "../db.json";

function Companies() {
  const news = data.companyNews;

  return (
    <div className="flex flex-col items-center justify-center h-screen p-4 bg-gray-100">
      <h1 className="text-4xl font-poppins mb-8">
        Top 10 Company News Articles
      </h1>
      <div className="w-full max-w-4xl">
        {news
          .sort((a, b) => a.id - b.id)
          .map((item, index) => (
            <div
              key={item.id}
              className="my-4 p-4 border rounded shadow bg-white"
            >
              <h2 className="text-2xl font-bold mb-2 text-center">
                {index + 1}. {item.title}
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

export default Companies;
