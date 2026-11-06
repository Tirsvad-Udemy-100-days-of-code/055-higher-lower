"""Tests of lecture step 5."""

from higher_lower.presentation.lectures.step_05_authenticated import (
    User,
    create_app,
    create_blog_post,
    is_authenticated,
)


def test_logged_in_user_can_create_a_post() -> None:
    user = User("Angela")
    user.is_logged_in = True
    assert create_blog_post(user) == "This is Angela's new blog post."


def test_logged_out_user_gets_no_post() -> None:
    assert create_blog_post(User("Bob")) is None


def test_user_can_be_passed_as_keyword() -> None:
    user = User("Angela")
    user.is_logged_in = True
    assert create_blog_post(user=user) == "This is Angela's new blog post."


def test_wrapper_forwards_extra_arguments() -> None:
    @is_authenticated
    def shout(user: User, word: str, times: int = 1) -> str:
        return f"{user.name}: {word * times}"

    user = User("Ann")
    user.is_logged_in = True
    assert shout(user, "hi", times=2) == "Ann: hihi"


def test_page_shows_both_users() -> None:
    body = create_app().test_client().get("/").get_data(as_text=True)
    assert "Angela is logged in: This is Angela&#39;s new blog post." in body
    assert "Bob is logged out: no post created" in body
