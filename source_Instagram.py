import instaloader

from instaloader import Profile

import pandas as pd

from base import Instagram

from typing import Optional


class SourceInstagram(Instagram):

    def __init__(self,
                 username: Optional[str] = None,
                 password: Optional[str] = None,
                 conn: Optional[bool] = False,
                 loader: Optional[instaloader.instaloader.Instaloader] = None,
                 profile: Optional[Profile] = None
                 ) -> None:
        super().__init__(username, password, conn, loader, profile)
        self.create_conn()


    def test_connector(self) -> bool:
        if not self.conn:
            self.create_conn()
        return True

    def __exit__(self):
        self.conn = None

    def get_followees(self, **kwargs):

        # If connection is not made, creating connection again
        if not self.conn:
            self.create_conn()

        # created followees list
        followees_lst = []

        # self.profile.get_followees() function returns the followees userid
        # All the followees user id's are being appended to list

        for followee in self.profile.get_followees():
            followees_lst.append(followee.username)

        pd.set_option('display.max_columns', 500)
        pd.set_option('display.max_rows', 500)

        # Created a pandas dataframe and converting the list to dataframe
        df = pd.DataFrame(followees_lst)

        # Dataframe of followees list is returned
        return df

    def get_followers(self, **kwargs):

        # If connection is not made, creating connection again
        if not self.conn:
            self.create_conn()

        # created followers list
        followers_list = []

        # self.profile.get_followers() function returns the followers userid
        # All the followers user id's are being appended to list

        for follower in self.profile.get_followers():
            followers_list.append(follower.username)

        pd.set_option('display.max_columns', 500)
        pd.set_option('display.max_rows', 500)

        # Created a pandas dataframe and converting the followers list to dataframe
        df = pd.DataFrame(followers_list)

        # Dataframe of followees list is returned
        return df

    def get_posts_details(self, **kwargs):

        # If connection is not made, creating connection again
        if not self.conn:
            self.create_conn()

        total_likes = 0
        total_comments = 0
        i = 0

        # created dictionary to store users individual post details
        dictionary = {}

        # profile.get_posts has the profile's posts information
        for post in self.profile.get_posts():

            # created a list to store the details of posts data
            lst = []

            # if post is of type video then video url, video view count , video duration
            # can be stored else details are filled as NA since post is not video type

            if post.is_video:
                lst.append(post.video_url)
                lst.append(post.video_view_count)
                lst.append(post.video_duration)
            else:
                lst.append("NA")
                lst.append("NA")
                lst.append("NA")
            total_likes += post.likes
            total_comments += post.comments
            i = i + 1

            # all the below details are being appended to the list
            lst.append(post.date_local)
            lst.append(post.url)
            lst.append(post.likes)
            lst.append(post.comments)
            lst.append(post.caption)
            lst.append(post.location)
            lst.append(post.tagged_users)

            # with post number being a key to the dictionary that we created, list will be the value for the post number
            dictionary[i] = lst

        pd.set_option('display.max_columns', 500)
        pd.set_option('display.max_rows', 500)

        # Created a dataframe and dictionary is converted into a dataframe
        df = pd.DataFrame(dictionary)

        # new dataframe is created that is the transpose of the dataframe
        # Rows of this new dataframe is the post number i.e., serial number
        # Columns of this new dataframe are the below details of post

        new_df = df.transpose()
        new_df.rename({
                       0: 'video url',
                       1: 'video view count',
                       2: 'video duration',
                       3: 'posted date',
                       4: 'url',
                       5: 'likes',
                       6: 'comments',
                       7: 'caption',
                       8: 'location',
                       9: 'users tagged in post'
                       }, axis=1, inplace=True)

        # Returning the new dataframe
        return new_df

