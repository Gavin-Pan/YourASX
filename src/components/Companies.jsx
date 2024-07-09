import React, { useState, useEffect } from "react";
import axios from "axios";

function Companies() {
  const [news, setNews] = useState({ companyNews: [] });
  const [loading, setLoading] = useState(true);

  const fetchNews = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:8080/newsletters");
      console.log("Fetched data:", res.data);
      setNews(res.data); // Set news data from API response
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchNews();
  }, []);

  // Render the fetched data
  return (
    <div className="flex flex-col items-center justify-center p-4 bg-gray-100 min-h-screen">
      <h1 className="text-4xl font-poppins mb-8">Top Company News Articles</h1>
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div className="w-full max-w-4xl">
          {news.companyNews.map((item, index) => (
            <div
              key={index}
              className="my-4 p-4 border rounded shadow bg-white"
            >
              <h3 className="text-2xl font-bold mb-2 text-center">
                {item.title}
              </h3>
              <p className="text-gray-600 mb-2 text-center">By {item.author}</p>
              <p className="text-gray-600 mb-2 text-center">
                ESG Score: {item.ESG}
              </p>
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
      )}
    </div>
  );
}

export default Companies;
