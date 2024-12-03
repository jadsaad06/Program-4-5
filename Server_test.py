#Name: Jad Saad
#File: Server_test.py

import pytest
from Server import Server
from Member import Admin, User, Mod, Permission

# Test for admin creating a channel
def test_adminCreateChannel():
    server = Server()
    admin = Admin("Admin")
    result = server.createChannel(admin, "general")
    assert result is True

# Test for creating a duplicate channel
def test_createDuplicateChannel():
    server = Server()
    admin = Admin("Admin")
    server.createChannel(admin, "general")
    result = server.createChannel(admin, "general")
    assert result is False

# Test for user creating a channel (should fail)
def test_userCreateChannel():
    server = Server()
    user = User("User")
    result = server.createChannel(user, "general")
    assert result is False

# Test for admin adding a user to a channel
def test_addUserToChannel():
    server = Server()
    admin = Admin("Admin")
    user = User("User")
    server.createChannel(admin, "general")
    result = server.addUserToChannel(admin, user, "general")
    assert result is True

# Test for posting a message to a channel
def test_postMessage():
    server = Server()
    admin = Admin("Admin")
    user = User("User")
    server.createChannel(admin, "general")
    server.addUserToChannel(admin, user, "general")
    result = server.postMessage(user, "general", "Hello, world!")
    assert result is True

# Test for posting a message without joining the channel
def test_postWithoutJoining():
    server = Server()
    user = User("User")
    server.createChannel(Admin("Admin"), "general")
    result = server.postMessage(user, "general", "Hello!")
    assert result is False

# Test for Mod scanning for prohibited content
def test_ModPermissions():
    mod = Mod("Moderator")
    assert mod.hasPermission(Permission.REMOVE_MESSAGE) is True
    assert mod.hasPermission(Permission.VIEW_FEED) is True
    assert mod.hasPermission(Permission.POST_MESSAGE) is True
    assert mod.hasPermission(Permission.CREATE_CHANNEL) is False
