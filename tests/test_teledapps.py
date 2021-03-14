import os


def test_bot():
    from teledapps import Bot

    bot = Bot()

    assert bot.updater is None


def test_passport():
    from teledapps.platform import Passport

    passport = Passport(
        name='Test',
        categories=[]
    )

    assert passport.name == 'Test'
    assert passport.categories == []


def test_get_active_account():
    from teledapps.platform import Platform

    os.environ['TELEDAPPS_ACCOUNT_ADDRESS'] = 'address'
    os.environ['TELEDAPPS_ACCOUNT_LABEL'] = 'label'

    platform = Platform()

    address, label = platform.get_active_account(1)

    assert address == 'address'
    assert label == 'label'


def test_dapp_default_keyboard():
    from teledapps.platform import helpers


# # def test_stages():
# #     print(teledapps.platform.helpers.basic_stage)
