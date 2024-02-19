# # import streamlit as st
# # from deta import Deta
# # import base64

# # # Initialize with a project key
# # DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
# # deta = Deta(DETA_KEY)

# # # Create Deta Base instance
# # my_db = deta.Base("BRIGHT_PSYCH_FORUM")

# # # Streamlit app
# # st.title('Community Forum')

# # # Sign-up / Registration page
# # if st.sidebar.checkbox('Register'):
# #     st.title('Registration')

# #     register_username = st.text_input('Enter a username:')
# #     register_password = st.text_input('Enter a password:', type='password')

# #     submit_registration = st.button('Submit Registration')

# #     if submit_registration:
# #         user = my_db.fetch({"Username": register_username}).items
# #         if not user:
# #             my_db.insert({"Username": register_username, "Password": register_password})
# #             st.success('Registration successful! Please sign in.')
# #         else:
# #             st.error('Username already exists. Choose a different username.')

# # # Sign-in
# # st.sidebar.title('Sign In')

# # sign_in_username = st.sidebar.text_input('Enter your username:')
# # sign_in_password = st.sidebar.text_input('Enter your password:', type='password')

# # if st.sidebar.button('Submit Sign In'):
# #     user = my_db.fetch({"Username": sign_in_username, "Password": sign_in_password}).items
# #     if user:
# #         st.session_state.logged_in = True
# #         st.session_state.username = sign_in_username
# #         st.sidebar.success(f'Welcome, {sign_in_username}!')
# #     else:
# #         st.sidebar.error('Invalid username or password. Please try again.')

# # # If the user is logged in, show forum functionalities
# # if getattr(st.session_state, 'logged_in', False):
# #     st.title('Community Forum')
# #     # Rest of the forum code ...

# #     # Post creation section
# #     st.title('Create a Post')

# #     # Input for text post
# #     new_post = st.text_area('Write your post here:', height=100)

# #     # Upload image for the post
# #     uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

# #     if st.button('Submit Post'):
# #         # Save the post to the database
# #         post_data = {"User": st.session_state.username, "Post": new_post}

# #         # If an image is uploaded, convert it to base64 and save in the database
# #         if uploaded_file:
# #             encoded_image = base64.b64encode(uploaded_file.read()).decode('utf-8')
# #             post_data['Image'] = encoded_image

# #         my_db.insert(post_data)
# #         st.success('Post submitted successfully!')

# #     # Display recent posts
# #     st.title('Recent Posts')

# #     # Assuming you have a Deta Base for forum posts
# #     posts_data = my_db.fetch({}).items

# #     for post in posts_data:
# #         user = post.get('User', 'Unknown User')
# #         st.write(f"**User:** {user}")
# #         st.write(f"**Post:** {post.get('Post', 'No post content')}")

# #         # Display image if available
# #         if 'Image' in post and post['Image']:
# #             st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

# #         # Add like, repost, share, and comment options (you can implement these functionalities)
# #         like_button_key = f"like_button_{user}_{post.get('PostID', '')}"  # Use a unique key
# #         repost_button_key = f"repost_button_{user}_{post.get('PostID', '')}"  # Use a unique key
# #         share_button_key = f"share_button_{user}_{post.get('PostID', '')}"  # Use a unique key
# #         comment_button_key = f"comment_button_{user}_{post.get('PostID', '')}"  # Use a unique key

# #         st.button('Like', key=like_button_key)
# #         st.button('Repost', key=repost_button_key)
# #         st.button('Share', key=share_button_key)
# #         st.button('Comment', key=comment_button_key)

# #         st.write('---')
# import streamlit as st
# from deta import Deta
# import base64

# # Initialize with a project key
# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
# deta = Deta(DETA_KEY)

# # Create Deta Base instance
# my_db = deta.Base("BRIGHT_PSYCH_FORUM")

# # Streamlit app
# st.title('Community Forum')

# # Sign-up / Registration page
# if st.sidebar.checkbox('Register'):
#     st.title('Registration')

#     register_username = st.text_input('Enter a username:')
#     register_password = st.text_input('Enter a password:', type='password')

#     submit_registration = st.button('Submit Registration')

#     if submit_registration:
#         user = my_db.fetch({"Username": register_username}).items
#         if not user:
#             my_db.insert({"Username": register_username, "Password": register_password})
#             st.success('Registration successful! Please sign in.')
#         else:
#             st.error('Username already exists. Choose a different username.')

# # Sign-in
# st.sidebar.title('Sign In')

# sign_in_username = st.sidebar.text_input('Enter your username:')
# sign_in_password = st.sidebar.text_input('Enter your password:', type='password')

# if st.sidebar.button('Submit Sign In'):
#     user = my_db.fetch({"Username": sign_in_username, "Password": sign_in_password}).items
#     if user:
#         st.session_state.logged_in = True
#         st.session_state.username = sign_in_username
#         st.sidebar.success(f'Welcome, {sign_in_username}!')
#     else:
#         st.sidebar.error('Invalid username or password. Please try again.')

# # If the user is logged in, show forum functionalities
# if getattr(st.session_state, 'logged_in', False):
#     st.title(f"Welcome, {st.session_state.username}!")

#     # Post creation section
#     st.title('Create a Post')

#     # Input for text post
#     new_post = st.text_area('Write your post here:', height=100)

#     # Upload image for the post
#     uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

#     if st.button('Submit Post'):
#         # Save the post to the database
#         post_data = {"User": st.session_state.username, "Post": new_post}

#         # If an image is uploaded, convert it to base64 and save in the database
#         if uploaded_file:
#             encoded_image = base64.b64encode(uploaded_file.read()).decode('utf-8')
#             post_data['Image'] = encoded_image

#         my_db.insert(post_data)
#         st.success('Post submitted successfully!')

#     # Display user's posts
#     st.title('Your Posts')

#     # Fetch and display posts by the logged-in user
#     user_posts = my_db.fetch({"User": st.session_state.username}).items

#     for post in user_posts:
#         st.write(f"**Post:** {post.get('Post', 'No post content')}")

#         # Display image if available
#         if 'Image' in post and post['Image']:
#             st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#         st.write('---')

#     # Display recent posts
#     st.title('Recent Posts')

#     # Assuming you have a Deta Base for forum posts
#     all_posts = my_db.fetch({}).items

#     for post in all_posts:
#         user = post.get('User', 'Unknown User')
#         st.write(f"**User:** {user}")
#         st.write(f"**Post:** {post.get('Post', 'No post content')}")

#         # Display image if available
#         if 'Image' in post and post['Image']:
#             st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#         # Add like, repost, share, and comment options (you can implement these functionalities)
#         like_button_key = f"like_button_{user}_{post.get('PostID', '')}"  # Use a unique key
#         repost_button_key = f"repost_button_{user}_{post.get('PostID', '')}"  # Use a unique key
#         share_button_key = f"share_button_{user}_{post.get('PostID', '')}"  # Use a unique key
#         comment_button_key = f"comment_button_{user}_{post.get('PostID', '')}"  # Use a unique key

#         st.button('Like', key=like_button_key)
#         st.button('Repost', key=repost_button_key)
#         st.button('Share', key=share_button_key)
#         st.button('Comment', key=comment_button_key)

#         st.write('---')
# import streamlit as st
# from deta import Deta
# import base64

# # Initialize with a project key
# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
# deta = Deta(DETA_KEY)

# # Create Deta Base instance
# my_db = deta.Base("BRIGHT_PSYCH_FORUM")

# # Streamlit app
# st.title('Community Forum')

# # Sign-up / Registration page
# if st.sidebar.checkbox('Register'):
#     st.title('Registration')

#     register_username = st.text_input('Enter a username:')
#     register_password = st.text_input('Enter a password:', type='password')

#     submit_registration = st.button('Submit Registration')

#     if submit_registration:
#         user = my_db.fetch({"Username": register_username}).items
#         if not user:
#             my_db.insert({"Username": register_username, "Password": register_password})
#             st.success('Registration successful! Please sign in.')
#         else:
#             st.error('Username already exists. Choose a different username.')

# # Sign-in
# st.sidebar.title('Sign In')

# sign_in_username = st.sidebar.text_input('Enter your username:')
# sign_in_password = st.sidebar.text_input('Enter your password:', type='password')

# if st.sidebar.button('Submit Sign In'):
#     user = my_db.fetch({"Username": sign_in_username, "Password": sign_in_password}).items
#     if user:
#         st.session_state.logged_in = True
#         st.session_state.username = sign_in_username
#         st.sidebar.success(f'Welcome, {sign_in_username}!')
#     else:
#         st.sidebar.error('Invalid username or password. Please try again.')

# # If the user is logged in, show forum functionalities
# if getattr(st.session_state, 'logged_in', False):
#     st.title(f"Welcome, {st.session_state.username}!")

#     # Post creation section
#     st.title('Create a Post')

#     # Input for text post
#     new_post = st.text_area('Write your post here:', height=100)

#     # Upload image for the post
#     uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

#     if st.button('Submit Post'):
#         # Save the post to the database
#         post_data = {"User": st.session_state.username, "Post": new_post, "Comments": []}

#         # If an image is uploaded, convert it to base64 and save in the database
#         if uploaded_file:
#             encoded_image = base64.b64encode(uploaded_file.read()).decode('utf-8')
#             post_data['Image'] = encoded_image

#         my_db.insert(post_data)
#         st.success('Post submitted successfully!')

#     # Display user's posts and allow comments
#    # Display user's posts and allow comments
# st.title('Your Posts')

# # Fetch and display posts by the logged-in user
# user_posts = my_db.fetch({"User": st.session_state.username}).items

# for post in user_posts:
#     st.write(f"**Post:** {post.get('Post', 'No post content')}")

#     # Display image if available
#     if 'Image' in post and post['Image']:
#         st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#     # Allow users to comment on the post
#     comment_input = st.text_input('Add a Comment:')
#     if st.button(f'Comment on Post {post.get("PostID", "")}', key=f'comment_button_{post.get("PostID", "")}'):
#         comment_data = {"User": st.session_state.username, "Comment": comment_input}
#         post['Comments'].append(comment_data)
#         my_db.update(post, post.get("PostID", ""))

#     # Display comments
#     for comment in post.get('Comments', []):
#         st.write(f"  - **{comment['User']}**: {comment['Comment']}")

#     st.write('---')

#     # Display recent posts with comments
#     st.title('Recent Posts')

#     # Assuming you have a Deta Base for forum posts
#     all_posts = my_db.fetch({}).items

#     for post in all_posts:
#         user = post.get('User', 'Unknown User')
#         st.write(f"**User:** {user}")
#         st.write(f"**Post:** {post.get('Post', 'No post content')}")

#         # Display image if available
#         if 'Image' in post and post['Image']:
#             st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#         # Allow users to comment on the post
#         comment_input = st.text_input('Add a Comment:')
#         if st.button(f'Comment on Post {post["_id"]}', key=f'comment_button_{post["_id"]}'):
#             comment_data = {"User": st.session_state.username, "Comment": comment_input}
#             post['Comments'].append(comment_data)
#             my_db.update(post, post["_id"])

#         # Display comments
#         for comment in post.get('Comments', []):
#             st.write(f"  - **{comment['User']}**: {comment['Comment']}")

#         st.write('---')
# import streamlit as st
# from deta import Deta
# import base64

# # Initialize with a project key
# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
# deta = Deta(DETA_KEY)

# # Create Deta Base instance
# my_db = deta.Base("BRIGHT_PSYCH_FORUM")

# # Streamlit app
# st.title('Community Forum')

# # Sign-up / Registration page
# if st.sidebar.checkbox('Register'):
#     st.title('Registration')

#     register_username = st.text_input('Enter a username:')
#     register_password = st.text_input('Enter a password:', type='password')

#     submit_registration = st.button('Submit Registration')

#     if submit_registration:
#         user = my_db.fetch({"Username": register_username}).items
#         if not user:
#             my_db.insert({"Username": register_username, "Password": register_password})
#             st.success('Registration successful! Please sign in.')
#         else:
#             st.error('Username already exists. Choose a different username.')

# # Sign-in
# st.sidebar.title('Sign In')

# sign_in_username = st.sidebar.text_input('Enter your username:')
# sign_in_password = st.sidebar.text_input('Enter your password:', type='password')

# if st.sidebar.button('Submit Sign In'):
#     user = my_db.fetch({"Username": sign_in_username, "Password": sign_in_password}).items
#     if user:
#         st.session_state.logged_in = True
#         st.session_state.username = sign_in_username
#         st.sidebar.success(f'Welcome, {sign_in_username}!')
#     else:
#         st.sidebar.error('Invalid username or password. Please try again.')

# # If the user is logged in, show forum functionalities
# if getattr(st.session_state, 'logged_in', False):
#     st.title(f"Welcome, {st.session_state.username}!")

#     # Post creation section
#     st.title('Create a Post')

#     # Input for text post
#     new_post = st.text_area('Write your post here:', height=100)

#     # Upload image for the post
#     uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

#     if st.button('Submit Post'):
#         # Save the post to the database
#         post_data = {"User": st.session_state.username, "Post": new_post}

#         # If an image is uploaded, convert it to base64 and save in the database
#         if uploaded_file:
#             encoded_image = base64.b64encode(uploaded_file.read()).decode('utf-8')
#             post_data['Image'] = encoded_image

#         my_db.insert(post_data)
#         st.success('Post submitted successfully!')

#     # Display user's posts and allow comments
#     st.title('Your Posts')

#     # Fetch and display posts by the logged-in user
#     user_posts = my_db.fetch({"User": st.session_state.username}).items

#     for post in user_posts:
#         st.write(f"**Post:** {post.get('Post', 'No post content')}")

#         # Display image if available
#         if 'Image' in post and post['Image']:
#             st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#         # Allow users to comment on the post
#         comment_input = st.text_input('Add a Comment:')
#         if st.button(f'Comment on Post {post.get("PostID", "")}', key=f'comment_button_{post.get("PostID", "")}'):
#             comment_data = {"User": st.session_state.username, "Comment": comment_input}
#             post['Comments'].append(comment_data)
#             my_db.update(post, post.get("PostID", ""))

#         # Display comments
#         for comment in post.get('Comments', []):
#             st.write(f"  - **{comment['User']}**: {comment['Comment']}")

#         st.write('---')

#     # Display recent posts with comments
#     st.title('Recent Posts')

#     # Assuming you have a Deta Base for forum posts
#     all_posts = my_db.fetch({}).items

#     for post in all_posts:
#         user = post.get('User', 'Unknown User')
#         st.write(f"**User:** {user}")
#         st.write(f"**Post:** {post.get('Post', 'No post content')}")

#         # Display image if available
#         if 'Image' in post and post['Image']:
#             st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#         # Allow users to comment on the post
#         comment_input = st.text_input('Add a Comment:')
#         if st.button(f'Comment on Post {post.get("PostID", "")}', key=f'comment_button_{post.get("PostID", "")}'):
#             comment_data = {"User": st.session_state.username, "Comment": comment_input}
#             post['Comments'].append(comment_data)
#             my_db.update(post, post.get("PostID", ""))

#         # Display comments
#         for comment in post.get('Comments', []):
#             st.write(f"  - **{comment['User']}**: {comment['Comment']}")

#         st.write('---')

# import streamlit as st
# from deta import Deta
# import base64

# # Initialize with a project key
# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
# deta = Deta(DETA_KEY)

# # Create Deta Base instance
# my_db = deta.Base("BRIGHT_PSYCH_FORUM")

# # Initialize session state
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
# if 'username' not in st.session_state:
#     st.session_state.username = None

# # Streamlit app
# st.title('Community Forum')

# # Sign-up / Registration page
# if st.sidebar.checkbox('Register'):
#     st.title('Registration')

#     register_username = st.text_input('Enter a username:')
#     register_password = st.text_input('Enter a password:', type='password')

#     submit_registration = st.button('Submit Registration')

#     if submit_registration:
#         user = my_db.fetch({"Username": register_username}).items
#         if not user:
#             my_db.insert({"Username": register_username, "Password": register_password})
#             st.success('Registration successful! Please sign in.')
#         else:
#             st.error('Username already exists. Choose a different username.')

# # Sign-in
# st.sidebar.title('Sign In')

# sign_in_username = st.sidebar.text_input('Enter your username:')
# sign_in_password = st.sidebar.text_input('Enter your password:', type='password')

# if st.sidebar.button('Submit Sign In'):
#     user = my_db.fetch({"Username": sign_in_username, "Password": sign_in_password}).items
#     if user:
#         st.session_state.logged_in = True
#         st.session_state.username = sign_in_username
#         st.sidebar.success(f'Welcome, {sign_in_username}!')
#     else:
#         st.sidebar.error('Invalid username or password. Please try again.')

# # If the user is logged in, show forum functionalities
# if st.session_state.logged_in:
#     st.title(f"Welcome, {st.session_state.username}!")

# # If the user is logged in, show forum functionalities
# if getattr(st.session_state, 'logged_in', False):
#     st.title(f"Welcome, {st.session_state.username}!")

#     # Post creation section
#     st.title('Create a Post')

#     # Input for text post
#     new_post = st.text_area('Write your post here:', height=100)

#     # Upload image for the post
#     uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

#     if st.button('Submit Post'):
#         # Save the post to the database
#         post_data = {"User": st.session_state.username, "Post": new_post}

#         # If an image is uploaded, convert it to base64 and save in the database
#         if uploaded_file:
#             encoded_image = base64.b64encode(uploaded_file.read()).decode('utf-8')
#             post_data['Image'] = encoded_image

#         my_db.insert(post_data)
#         st.success('Post submitted successfully!')

# # ... (previous code)

# # Display user's posts and allow comments
# st.title('Your Posts')

# # Fetch and display posts by the logged-in user
# user_posts = my_db.fetch({"User": st.session_state.username}).items

# for post in user_posts:
#     st.write(f"**Post:** {post.get('Post', 'No post content')}")

#     # Display image if available
#     if 'Image' in post and post['Image']:
#         st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#     comment_input_ke_1 = f'comment_input_{post.get("PostID", "")}'
#     comment_input = st.text_input(f'Add a Comment for Post {post.get("PostID", "")}:', key=comment_input_ke_1)

#     if 'Comments' not in post:
#         post['Comments'] = []  # Initialize 'Comments' if not present

#     comment_button_key = f'comment_button_{post.get("PostID", "")}'

#     if st.button(f'Comment on Post {post.get("PostID", "")}', key=comment_button_key):
#         comment_data = {"User": st.session_state.username, "Comment": comment_input}
#         post['Comments'].append(comment_data)

#     # Check if the post has a valid PostID before updating
#     if "PostID" in post and post["PostID"]:
#         my_db.update(post, post["PostID"])
#     else:
#         st.warning("Unable to update post: PostID is missing or empty.")
#     st.write('---')
    
#     # Display comments
#     for comment in post.get('Comments', []):
#         st.write(f"  - **{comment['User']}**: {comment['Comment']}")

# # Display recent posts with comments
# st.title('Recent Posts')

# # Assuming you have a Deta Base for forum posts
# all_posts = my_db.fetch({}).items

# for post in all_posts:
#     user = post.get('User', 'Unknown User')
#     st.write(f"**User:** {user}")
#     st.write(f"**Post:** {post.get('Post', 'No post content')}")

#     # Display image if available
#     if 'Image' in post and post['Image']:
#         st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#     # Allow users to comment on the post
#     comment_input_ky_2 = f'comment_input_{post.get("PostID", "")}'
#     comment_inpu = st.text_input(f'Add a Comment for Post {post.get("PostID", "")}:', key=comment_input_ky_2)

#     if 'Comments' not in post:
#         post['Comments'] = []  # Initialize 'Comments' if not present

#     comment_button_key = f'comment_button_{post.get("PostID", "")}'

#     if st.button(f'Comment on Post {post.get("PostID", "")}', key=comment_button_key):
#         comment_data = {"User": st.session_state.username, "Comment": comment_input}
#         post['Comments'].append(comment_data)

#     # Check if the post has a valid PostID before updating
#     if "PostID" in post and post["PostID"]:
#         my_db.update(post, post["PostID"])
#     else:
#         st.warning("Unable to update post: PostID is missing or empty.")
#     st.write('---')
    
#     # Display comments
#     for comment in post.get('Comments', []):
#         st.write(f"  - **{comment['User']}**: {comment['Comment']}")

#     st.write('---')# Display user's posts and allow comments
# # Display user's profile, including their posts and comments
# st.title('Your Profile')

# # Fetch and display posts by the logged-in user
# user_posts = my_db.fetch({"User": st.session_state.username}).items

# for post in user_posts:
#     st.write(f"**Post:** {post.get('Post', 'No post content')}")

#     # Display image if available
#     if 'Image' in post and post['Image']:
#         st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#     comment_input_key = f'comment_input_{post.get("PostID", "")}'
#     comment_input = st.text_input(f'Add a Comment for Post {post.get("PostID", "")}:', key=comment_input_key)

#     if 'Comments' not in post:
#         post['Comments'] = []  # Initialize 'Comments' if not present

#     comment_button_key = f'comment_button_{post.get("PostID", "")}'

#     if st.button(f'Comment on Post {post.get("PostID", "")}', key=comment_button_key):
#         comment_data = {"User": st.session_state.username, "Comment": comment_input, "PostID": post.get("PostID", "")}
#         my_db.insert(comment_data)

#     st.write('---')
    
#     # Display comments
#     for comment in post.get('Comments', []):
#         st.write(f"  - **{comment['User']}**: {comment['Comment']}")

# st.write('---')

# # Display recent posts with comments
# st.title('Recent Posts')

# # Assuming you have a Deta Base for forum posts
# all_posts = my_db.fetch({}).items

# for post in all_posts:
#     user = post.get('User', 'Unknown User')
#     st.write(f"**User:** {user}")
#     st.write(f"**Post:** {post.get('Post', 'No post content')}")

#     # Display image if available
#     if 'Image' in post and post['Image']:
#         st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#     # Retrieve comments for the post from the comments collection
#     comments_for_post = my_db.fetch({"PostID": post.get("PostID", "")}).items

#     for comment in comments_for_post:
#         st.write(f"  - **{comment['User']}**: {comment['Comment']}")

#     # Allow users to comment on the post
#     comment_input_key = f'comment_input_{post.get("PostID", "")}'
#     comment_input = st.text_input(f'Add a Comment for Post {post.get("PostID", "")}:', key=comment_input_key)

#     if 'Comments' not in post:
#         post['Comments'] = []  # Initialize 'Comments' if not present

#     comment_button_key = f'comment_button_{post.get("PostID", "")}'

#     if st.button(f'Comment on Post {post.get("PostID", "")}', key=comment_button_key):
#         comment_data = {"User": st.session_state.username, "Comment": comment_input, "PostID": post.get("PostID", "")}
#         my_db.insert(comment_data)

#     st.write('---')

#     # Display comments
#     for comment in post.get('Comments', []):
#         st.write(f"  - **{comment['User']}**: {comment['Comment']}")

#     st.write('---')

# import streamlit as st
# from deta import Deta
# import base64

# # Initialize with a project key
# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
# deta = Deta(DETA_KEY)

# # Create Deta Base instance
# my_db = deta.Base("BRIGHT_PSYCH_FORUM")

# # Initialize session state
# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False
# if 'username' not in st.session_state:
#     st.session_state.username = None

# # Streamlit app
# st.title('Community Forum')

# # Sidebar navigation
# page = st.sidebar.selectbox("Navigation", ["Feed", "Profile"])

# # Feed page
# if page == "Feed":
#     st.title('Recent Posts')

#     # Assuming you have a Deta Base for forum posts
#     all_posts = my_db.fetch({}).items

#     for post in all_posts:
#         user = post.get('User', 'Unknown User')
#         st.write(f"**User:** {user}")
#         st.write(f"**Post:** {post.get('Post', 'No post content')}")

#         # Display image if available
#         if 'Image' in post and post['Image']:
#             st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#         # Retrieve comments for the post from the comments collection
#         comments_for_post = my_db.fetch({"PostID": post.get("PostID", "")}).items

#         for comment in comments_for_post:
#             st.write(f"  - **{comment['User']}**: {comment['Comment']}")

#         # Allow users to comment on the post
#         comment_input_key = f'comment_input_{post.get("PostID", "")}'
#         comment_input = st.text_input(f'Add a Comment for Post {post.get("PostID", "")}:', key=comment_input_key)

#         if 'Comments' not in post:
#             post['Comments'] = []  # Initialize 'Comments' if not present

#         comment_button_key = f'comment_button_{post.get("PostID", "")}'

#         if st.button(f'Comment on Post {post.get("PostID", "")}', key=comment_button_key):
#             comment_data = {"User": st.session_state.username, "Comment": comment_input, "PostID": post.get("PostID", "")}
#             my_db.insert(comment_data)

#         st.write('---')

#         # Display comments
#         for comment in post.get('Comments', []):
#             st.write(f"  - **{comment['User']}**: {comment['Comment']}")

#         st.write('---')

# # Profile page
# elif page == "Profile":
#     st.title('Your Profile')

#     # Fetch and display posts by the logged-in user
#     user_posts = my_db.fetch({"User": st.session_state.username}).items

#     for post in user_posts:
#         st.write(f"**Post:** {post.get('Post', 'No post content')}")

#         # Display image if available
#         if 'Image' in post and post['Image']:
#             st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#         comment_input_key = f'comment_input_{post.get("PostID", "")}'
#         comment_input = st.text_input(f'Add a Comment for Post {post.get("PostID", "")}:', key=comment_input_key)

#         if 'Comments' not in post:
#             post['Comments'] = []  # Initialize 'Comments' if not present

#         comment_button_key = f'comment_button_{post.get("PostID", "")}'

#         if st.button(f'Comment on Post {post.get("PostID", "")}', key=comment_button_key):
#             comment_data = {"User": st.session_state.username, "Comment": comment_input, "PostID": post.get("PostID", "")}
#             my_db.insert(comment_data)

#         st.write('---')

#         # Display comments
#         for comment in post.get('Comments', []):
#             st.write(f"  - **{comment['User']}**: {comment['Comment']}")

#         st.write('---')

# import streamlit as st
# from deta import Deta
# import base64

# if 'logged_in' not in st.session_state:
#     st.session_state.logged_in = False

# if 'username' not in st.session_state:
#     st.session_state.username = None
    
# def display_and_handle_comments(post):
#     comment_input_key = f'comment_input_{post.get("key", "")}_{st.session_state.username}'
#     # check_duplicate_key(comment_input_key)  # Check for duplicate key
#     print("Hello")
#     comment_input = st.text_input(f'Add a Comment for Post {post.get("PostID", "")}:', key=comment_input_key)

#     if 'Comments' not in post:
#         post['Comments'] = []  # Initialize 'Comments' if not present

#     comment_button_key = f'comment_button_{post.get("key", "")}'
#     # check_duplicate_key(comment_button_key)  # Check for duplicate key
#     if st.button(f'Comment on Post {post.get("PostID", "")}', key=comment_button_key):
#         comment_data = {"User": st.session_state.username, "Comment": comment_input, "PostID": post.get("PostID", "")}
#         post['Comments'].append(comment_data)

#     # Check if the post has a valid PostID before updating
#     if "PostID" in post and post["PostID"]:
#         my_db.update(post, post["PostID"])
#     else:
#         st.warning("Unable to update post: PostID is missing or empty.")

# # Define a function to check for duplicate keys
# # def check_duplicate_key(key):
# #     if key in st.session_state:
# #         st.warning(f'Duplicate key detected: {key}. Please ensure keys are unique.')

# # Define a function to display comments
# def display_comments(post):
#     # Display comments
#     for comment in post.get('Comments', []):
#         st.write(f"  - **{comment['User']}**: {comment['Comment']}")

# # Initialize with a project key
# DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
# deta = Deta(DETA_KEY)

# # Create Deta Base instance
# my_db = deta.Base("BRIGHT_PSYCH_FORUM")

# # Streamlit app
# st.title('Community Forum')

# # Sidebar navigation
# page = st.sidebar.selectbox("Navigation", ["Feed", "Profile"])

# # Feed page
# if page == "Feed":
#     st.title('Recent Posts')

#     # Assuming you have a Deta Base for forum posts
#     all_posts = my_db.fetch({}).items

#     for post in all_posts:
#         user = post.get('User', 'Unknown User')
#         st.write(f"**User:** {user}")
#         st.write(f"**Post:** {post.get('Post', 'No post content')}")

#         # Display image if available
#         if 'Image' in post and post['Image']:
#             st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#         # Retrieve comments for the post from the comments collection
#         comments_for_post = my_db.fetch({"PostID": post.get("PostID", "")}).items

#         for comment in comments_for_post:
#             st.write(f"  - **{comment['User']}**: {comment['Comment']}")

#         # Allow users to comment on the post
#         display_and_handle_comments(post)

#         st.write('---')

#         # Display comments
#         display_comments(post)

#         st.write('---')

# # Recent Posts page
# elif page == "Profile":
#     st.title('Your Profile')

#     if not st.session_state.logged_in:
#         st.sidebar.warning('Please sign in to view your profile.')

#         # Sign-in
#         st.sidebar.title('Sign In')

#         sign_in_username = st.sidebar.text_input('Enter your username:')
#         sign_in_password = st.sidebar.text_input('Enter your password:', type='password')

#         if st.sidebar.button('Submit Sign In'):
#             user = my_db.fetch({"Username": sign_in_username, "Password": sign_in_password}).items
#             if user:
#                 st.session_state.logged_in = True
#                 st.session_state.username = sign_in_username
#                 st.sidebar.success(f'Welcome, {sign_in_username}!')
#             else:
#                 st.sidebar.error('Invalid username or password. Please try again.')

#         # Register if not signed in
#         st.sidebar.title('Register')
#         register_username = st.sidebar.text_input('Enter a new username:')
#         register_password = st.sidebar.text_input('Enter a password for registration:', type='password')
        
#         if st.sidebar.button('Register'):
#             # Check if the username is available
#             if not my_db.fetch({"Username": register_username}).items:
#                 # Register the new user
#                 my_db.insert({"Username": register_username, "Password": register_password})
#                 st.sidebar.success('Registration successful! You can now sign in.')
#             else:
#                 st.sidebar.warning('Username already exists. Please choose a different username.')


#     if st.session_state.logged_in:
#         # Fetch and display posts by the logged-in user
#         user_posts = my_db.fetch({"User": st.session_state.username}).items

#         for post in user_posts:
#             st.write(f"**Post:** {post.get('Post', 'No post content')}")

#             # Display image if available
#             if 'Image' in post and post['Image']:
#                 st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

#             # Display and handle comments
#             display_and_handle_comments(post)

#             # Display comments
#             display_comments(post)

#             # Check if the post has a valid PostID before updating
#             if "PostID" in post and post["PostID"]:
#                 my_db.update(post, post["PostID"])
#             else:
#                 st.warning("Unable to update post: PostID is missing or empty.")

#             st.write('---')
import streamlit as st
from deta import Deta
import base64
import uuid

st.markdown(
    """
    <style>
    .main{
        background: #4a5566;
    }
    
    </style>
    
    """,unsafe_allow_html=True
)

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'username' not in st.session_state:
    st.session_state.username = None

def generate_unique_comment_id():
    return str(uuid.uuid4())

def generate_unique_post_id():
    return str(uuid.uuid4())

def handle_new_post(session_state):
    st.title('Create a Post')

    key = "lweotweopitwiop"

    text_input_key = f'text_input_{key}_{st.session_state.username}'
    submit_input_key = f'submit_input_{key}_{st.session_state.username}'
    img_input_key = f'img_input_{key}_{st.session_state.username}'

    # Input for text post
    new_post = st.text_area('Write your post here:', height=100, key=text_input_key)

    # Upload image for the post
    uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"], key=img_input_key)

    if st.button('Submit Post', key=submit_input_key):
        # Save the post to the database
        post_data = {
            "User": st.session_state.username,
            "Post": new_post,
            "key": key,  # Use "key" as the unique identifier
            "Comments": []  # Initialize an empty list for comments
        }

        # If an image is uploaded, convert it to base64 and save in the database
        if uploaded_file:
            encoded_image = base64.b64encode(uploaded_file.read()).decode('utf-8')
            post_data['Image'] = encoded_image

        my_db.insert(post_data)
        st.success('Post submitted successfully!')
        
        
def display_and_handle_comments(post, parent_comment=None):
    if parent_comment:
        comment_input_key = f'comment_input_{post.get("key", "")}{st.session_state.username}{parent_comment.get("CommentID", "")}'
        comment_button_key = f'comment_button_{post.get("key", "")}{st.session_state.username}{parent_comment.get("CommentID", "")}'
    else:
        comment_input_key = f'comment_input_{post.get("key", "")}_{st.session_state.username}'
        comment_button_key = f'comment_button_{post.get("key", "")}_{st.session_state.username}'

    comment_input = st.text_input(f'Add a Comment for Post {post.get("PostID", "")}:', key=comment_input_key)

    if 'Comments' not in post:
        post['Comments'] = []  # Initialize 'Comments' if not present

    if st.button(f'Comment on Post {post.get("PostID", "")}', key=comment_button_key):
        comment_data = {
            "User": st.session_state.username,
            "Comment": comment_input,
            "PostID": post.get("PostID", ""),
            "CommentID": generate_unique_comment_id(),
        }

        if parent_comment:
            comment_data["ParentCommentID"] = parent_comment.get("CommentID", "")

        post['Comments'].append(comment_data)

    # Check if the post has a valid PostID before updating
    if "PostID" in post and post["PostID"]:
        my_db.update(post, post["PostID"])
    else:
        st.warning("Unable to update post: PostID is missing or empty.")

    # Display child comments
    for comment in post.get('Comments', []):
        if parent_comment and comment.get("ParentCommentID") == parent_comment.get("CommentID"):
            st.write(f"  - {comment['User']}: {comment['Comment']}")
            display_and_handle_comments(post, parent_comment=comment)

def display_comments(post):
    # Display top-level comments
    for comment in post.get('Comments', []):
        if "ParentCommentID" not in comment:
            st.write(f"  - {comment['User']}: {comment['Comment']}")
            display_and_handle_comments(post, parent_comment=comment)

# Initialize with a project key
DETA_KEY = "d0z8gryt9dj_HMVcfkbW7ZYYVeyz3xakbf48ZZGAxUtp"
deta = Deta(DETA_KEY)

# Create Deta Base instance
my_db = deta.Base("BRIGHT_PSYCH_FORUM")

# Streamlit app
if st.session_state.logged_in:
    st.title('Community Forum')

# Sidebar navigation
page = st.sidebar.selectbox("Navigation", ["Feed", "Profile"])

# Feed page
if page == "Feed":
    st.title('Recent Posts')

    # Assuming you have a Deta Base for forum posts
    all_posts = my_db.fetch({}).items

    for post in all_posts:
        user = post.get('User', 'Unknown User')
        st.write(f"User: {user}")
        st.write(f"Post: {post.get('Post', 'No post content')}")

        # Display image if available
        if 'Image' in post and post['Image']:
            st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

        # Retrieve comments for the post from the comments collection
        comments_for_post = my_db.fetch({"PostID": post.get("PostID", "")}).items

        for comment in comments_for_post:
            if comment.get("ParentCommentID") is None:
                st.write(f"  - {comment['User']}: {comment['Comment']}")
                display_and_handle_comments(post, parent_comment=comment)
                display_comments(post, parent_comment=comment)

        st.write('---')

# Recent Posts page
elif page == "Profile":
    st.title('Your Profile')

    if not st.session_state.logged_in:
        st.sidebar.warning('Please sign in to view your profile.')

        # Sign-in
        st.sidebar.title('Sign In')

        sign_in_username = st.sidebar.text_input('Enter your username:')
        sign_in_password = st.sidebar.text_input('Enter your password:', type='password')

        if st.sidebar.button('Submit Sign In'):
            user = my_db.fetch({"Username": sign_in_username, "Password": sign_in_password}).items
            if user:
                st.session_state.logged_in = True
                st.session_state.username = sign_in_username
                st.sidebar.success(f'Welcome, {sign_in_username}!')
            else:
                st.sidebar.error('Invalid username or password. Please try again.')

        # Register if not signed in
        st.sidebar.title('Register')
        register_username = st.sidebar.text_input('Enter a new username:')
        register_password = st.sidebar.text_input('Enter a password for registration:', type='password')
        
        if st.sidebar.button('Register'):
            # Check if the username is available
            if not my_db.fetch({"Username": register_username}).items:
                # Register the new user
                my_db.insert({"Username": register_username, "Password": register_password})
                st.sidebar.success('Registration successful! You can now sign in.')
            else:
                st.sidebar.warning('Username already exists. Please choose a different username.')

        # Display new post form
        handle_new_post(st.session_state)

    elif page == "Profile":
        st.title('Your Profile')

    if not st.session_state.logged_in:
        st.sidebar.warning('Please sign in to view your profile.')

        # ... (existing code for sign-in and registration)

    else:  # If the user is logged in
        # Display new post form
        handle_new_post(st.session_state)

        # Fetch and display posts by the logged-in user
        user_posts = my_db.fetch({"User": st.session_state.username}).items

        if not user_posts:
            st.write("You haven't made any posts yet.")

        for post in user_posts:
            st.write(f"Post ID: {post.get('PostID', 'No ID')}")  # Display Post ID
            st.write(f"Post: {post.get('Post', 'No post content')}")

            # Display image if available
            if 'Image' in post and post['Image']:
                st.image(base64.b64decode(post['Image']), caption='Uploaded Image', use_column_width=True)

            # Display and handle comments
            display_and_handle_comments(post)

            # Display comments
            display_comments(post)

            # Check if the post has a valid PostID before updating
            if "PostID" in post and post["PostID"]:
                my_db.update(post, post["PostID"])
            else:
                st.warning("Unable to update post: PostID is missing or empty.")

            st.write('---')