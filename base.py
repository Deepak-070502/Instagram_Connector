import instaloader

from instaloader import Profile

from aifc import Error

from typing import Optional


class Instagram:
    def __init__(
            self,
            username: Optional[str] = None,
            password: Optional[str] = None,
            conn: Optional[bool] = False,
            loader: Optional[instaloader.instaloader.Instaloader] = None,
            profile: Optional[Profile] = None
            ) -> None:
        if not conn:
            self.conn = None
        elif conn:
            self.conn = conn

        self.username = username
        self.password = password
        self.conn = False
        self.loader = None
        self.profile = None

    def create_conn(self):
        try:

            # Instaloader instance is being created
            # loader is an instance of this module

            loader = instaloader.Instaloader()

            # using the username and password of the user, we login to the instagram

            loader.login(self.username, self.password)

            # profile metadata is stored by fetching the data from Profile class for a particular user

            self.profile = Profile.from_username(loader.context, self.username)

            # Connection is made as logging in is done

            self.conn = True

            # Uncomment the below code to see the object of type for loader and profile
            # loader is an object in instaloader.instaloader.Instaloader
            # profile is an object inProfile class


            print(loader)
            print(self.profile)

        except Error as e:
            print(e)

        
