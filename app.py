import streamlit as st
from crawl4ai import WebCrawler
import base64

# Function to generate a download link for the extracted markdown content
def download_markdown(content, filename="extracted_content.md"):
      # Encode the content as base64
    b64 = base64.b64encode(content.encode()).decode()
    # Create a download link for the markdown file
    href = f'<a href="data:file/markdown;base64,{b64}" download="{filename}">Download Markdown File</a>'
    return href

# Streamlit App
def main():
    st.title("Crawl4AI Web Scraper")

    # URL input
    url = st.text_input("Enter the URL you want to scrape:")

    # Button to start the crawl
    if st.button("Run Crawl"):
        if url:
            # Create an instance of WebCrawler and warm it up (load necessary models)
            crawler = WebCrawler()
            crawler.warmup()

            # Run the crawler and display the result in markdown format
            result = crawler.run(url=url)
            st.markdown(result.markdown)

            # Download markdown file
            st.markdown(download_markdown(result.markdown), unsafe_allow_html=True)
        else:
            st.warning("Please enter a valid URL.")

if __name__ == "__main__":
    main()
