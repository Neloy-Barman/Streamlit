import streamlit as st


"""
    Cache Duration: - 
        We can control the cache duration. 
        Sometimes, objects in the cache can become outdated.
        For example, the database can get updated with new but but working with old cached query.
        We can use (ttl - time to live) parameter. It simply represents time in seconds that must be elapsed
        to update the function again and update the cache.
"""
# It will refresh the cache after 1 h.
@st.cache_data(ttl=3600)
def show():
    return "Hello world"


"""
    Cache Size: - 
        Caching many large objects will cause the cache to run out of memory.
        We can use max_entries parameter we can control that and discard old values to keep space
        in the cache. 
"""
@st.cache_data(max_entries=1000)
def show():
    return "Hello world"


"""
    Customize the spinner: - 
        Disable the showing off spinner.
        Show a customized message.
"""
@st.cache_data(show_spinner=False)
@st.cache_data(show_spinner="Custom spinner text")
def show():
    return "Hello world"


"""
    Exclude input parameters: - 
        The input parameters in the cache must be hashable.
        In this way, streamlit checks if the input parameters are new or it can simply return the cached result.
        Not all parameters can be hashed. For example, a model is not hashable. 
        Therefore, we can proceed it using an underscore to tell streamlit not to hash.
        In that way, the streamlit will check if other parameters changed. 
"""
@st.cache_data
def make_predictions(_model, x_pred):
    preds = _model.predict(x_pred)
    return preds

