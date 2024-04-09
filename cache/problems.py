import streamlit as st

# We are caching a funcion that returns a list.
@st.cache_resource
def create_list():
    l = [1,2,3]
    return l

l = create_list()

# Mutation issue
# Mutate the list
l = l.remove(1)
st.write(l)

"""
    As we are using cache_resource, we are mutating the output in the cache.
    So, the first time, the app runs, it will work fine.
    But on the second run, the app will crash.
    Because we are trying to remove an element from a list that doesn't exist anymore.
    That's why we must use cache_data here.
    With cache_data we will be working with a copy of the result, the output will work with all users and all sessions. 
"""

# Concurrency issue
l = create_list()
l[0] = l[0] + 1
st.write(l)

"""
    Suppose, 3 users are using our app.
    The first user runs the app and the result becomes [2,2,3].
    If another user runs the app right after the caching, he will see [3,2,3].
    In the same way another one will see [4,2,3].
    So, we should use cache_data, so that we work with copy and the copy is then sent to the browser.
    Each user works with their different copy.
"""

