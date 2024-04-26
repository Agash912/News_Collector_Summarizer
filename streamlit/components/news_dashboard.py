import streamlit as st
import configparser
import requests

config = configparser.ConfigParser()
config.read('./configuration.properties')
base_url = config['APIs']['base_url']

def news_nest_app():


    st.title(":red[NewsNest: Curated Summaries Hub]")

    # Search input
    # st.text_input("Search")

    # categories = [
    #     ["Education", "Environment", "International", "Technology", "Entertainment"],
    #     ["United-States", "Middle-east", "Europe", "India", "World"],
    #     ["Football", "Golf", "Job", "Sports", "Politics", "Health", "Art"],
    #     ["Elections", "Business", "Top News", "Olympics", "Tennis"]
    # ]

    # Flatten the categories list for dropdown
    # category_options = [item for sublist in categories for item in sublist if item]

    # Selectbox for categories
    # selected_category = st.selectbox("Select Category", category_options)

    url = base_url + '/news'
    access_token = st.session_state["access_token"]
    token_type = st.session_state["token_type"]
    # Making the POST request
    headers = {
        "Authorization": "{} {}".format(token_type, access_token),
        'Content-Type': 'application/json',
    }
    response = requests.get(url, headers=headers)
    
    news_data = []
    for result in response['result']:
        formatted_result = {}
        formatted_result['Title'] = result.get('TITLE',"")
        formatted_result['Link'] = result.get('LINK',"")
        formatted_result['Description'] = result.get('DESCRIPTION',"")
        formatted_result['Image_url'] = result.get('IMAGE_URL',"")
        formatted_result['Source'] = result.get('SOURCE',"")
        formatted_result['Publish_Date'] = result.get('PUBLISH_DATE',"")
        news_data.append(formatted_result)
        
        
    
    
    # Sample news data
    # news_data = [
    #     {"Title": "Breaking News 1", "image": "https://via.placeholder.com/150", "source": "Description of Breaking News ", "PUBLISH_DATE":""}
    # ]

    # Function to display pop-up card
    def display_popup_card(news_item):
        st.write("### " + news_item["Title"])
        st.image(news_item["Image"], use_column_width=True)
        st.write(news_item["Source"])
        st.write(news_item["Publish_date"])
        st.write(news_item["Description"])

        # Add a close button
        if st.button("Close"):
            st.write("Popup closed.")

    col_count = 4
    for i in range(0, len(news_data), col_count):
        cols = st.columns(col_count)
        for j in range(col_count):
            if i + j < len(news_data):
                with cols[j]:
                    st.image(news_data[i + j]["Image_url"], use_column_width=True)
                    if st.button(news_data[i + j]["Title"]):
                        selected_news = news_data[i + j]
                        st.write("---")
                        display_popup_card(selected_news)

# Run the Streamlit app
if __name__ == "__main__":
    news_nest_app()