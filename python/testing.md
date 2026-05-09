# 🧩 1. What is mock?

A mock is: A fake version of a real object used in tests.

Instead of calling real AWS:

boto3.Session(...)

we replace it with a fake object that:

- does not call AWS
- records how it was used
- returns controlled data

With mocking:

No AWS needed ✅
Fast execution ✅
Fully controlled behavior ✅
Deterministic results ✅

# Example


from unittest.mock import patch

from modules.boto3_session import GetSession


@patch("modules.boto3_session.boto3.Session")
def test_get_session_uses_profile_and_region(mock_session_ctor) -> None:
    expected_session = object()
    mock_session_ctor.return_value = expected_session

    result = GetSession("1006-cloud-adm", "ap-southeast-2").get_session()

    mock_session_ctor.assert_called_once_with(
        profile_name="1006-cloud-adm",
        region_name="ap-southeast-2",
    )
    assert result is expected_session

- mock_session_ctor : is a mock version of boto3.Session. 
  So instead of creating a real AWS session, it returns expected_session = object()

# What is patch?

@patch("modules.boto3_session.boto3.Session")

patch means: “temporarily replace this real object with a mock during the test”

modules.boto3_session.boto3.Session is replaced with a mock.

So inside your module boto3.Session(...) becomes mock_session_ctor(...)

# 🧠 3. What happens step by step

Step 1: patch activates

@patch("modules.boto3_session.boto3.Session") 

👉 Replaces: boto3.Session  with mock_session_ctor

Step 2: mock is injected into test

def test_get_session_uses_profile_and_region(mock_session_ctor)

pytest/unittest automatically passes the mock in.

Step 3: configure mock behavior

expected_session = object()
mock_session_ctor.return_value = expected_session

Meaning: “When Session() is called, return this object instead of real AWS session”

Step 4: run real code
result = GetSession("1006-cloud-adm", "ap-southeast-2").get_session()

Inside your class: boto3.Session(profile_name=..., region_name=...)

BUT now it's actually: mock_session_ctor(...)

Step 5: verify call happened correctly

mock_session_ctor.assert_called_once_with(
    profile_name="1006-cloud-adm",
    region_name="ap-southeast-2",
)

This checks: 👉 Did your code call Session correctly?

Step 6: verify return value

assert result is expected_session

This checks: 👉 Did your method return whatever boto3.Session returned?
