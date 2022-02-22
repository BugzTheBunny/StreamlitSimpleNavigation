# StreamlitSimpleNavigation
A simple navigation example

The navigation can be a bit slow, for a fast navigation please use [THIS](https://discuss.streamlit.io/t/streamlit-navbar/14936) I'ts faster but uses Flask.

Structure:

- `.streamlit` - contains the streamlit configuration [More here](https://docs.streamlit.io/library/advanced-features/configuration).

- `static` - contains static files, for example it contains a `styles.css` file which is injected into the page, you can use it to style the application, it's already being injected in the code.

- `views` - the views of the application, you can drop views there, import them in `utilities.py` and then navigate with them, that's how you can create different views easy.

- `application.py` - This is the start point, it contains the injection of the CSS + the navigation component.

- `utilities.py` - a file for utilities for the application.