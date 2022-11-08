# Dev page

!!! info

    This page is only for the development environment. You could create projects
    and switch account sessions here.

## Enter the dev page

Visit the dev page to setup.

    http://127.0.0.1:80/dev/

## Assign the owner

Before going to the following steps, you need to assign the uid as the owner in the `setting.py`.

``` python
API_DEFAULT_OWNERS = ['00000000', ]  # replace `00000000` to your uid.
```

## Accounts

Default will create 10 accounts for developing.

<figure markdown>
  <a href="https://s3.toomore.net/coscup/volunteer/docs_dev_account_lists.png">
    <img alt="docs_dev_account_lists"
         src="https://s3.toomore.net/coscup/volunteer/docs_dev_account_lists.png"
         style="border: 1px #ececec solid; border-radius: 0.4rem;"
    >
  </a>
</figure>

## Sessions

In the sessions section, there are 10 account lists by default. You can switch
those account sessions by clicking the button.

## Projects

You need to create the first project for you to develop. Please click
the `To create a project` to toggle the creating form.

<figure markdown>
  <a href="https://s3.toomore.net/coscup/volunteer/docs_create_project.png">
    <img alt="docs_create_project"
         src="https://s3.toomore.net/coscup/volunteer/docs_create_project.png"
         style="border: 1px #ececec solid; border-radius: 0.4rem;"
    >
  </a>
</figure>

The example can follow this setting:

- `pid` as `2022`
- `name` as `One Project`
- `action date` could be any time.

... and then click `Create Project`.

The new project will be shown on the Project lists. Click `Setting` to
enter the setting page.

## Edit Project

In this section, you will learn how to create a team in the project.

Go to the project page: `http://127.0.0.1/project/{pid}/edit`.

Click `編輯組別`, and click `建立` to toggle the dialog box. The example can follow this setting:

- name as `One Team`
- tid as `one`

... and click `update`

### Add chiefs or members

Click `編輯` after the team list. Typing the user id (`uid`) into the fields of `chiefs`, `members`.

<figure markdown>
  <a href="https://s3.toomore.net/coscup/volunteer/docs_edit_team_setting.png">
    <img alt="docs_edit_team_setting"
         src="https://s3.toomore.net/coscup/volunteer/docs_edit_team_setting.png"
         style="border: 1px #ececec solid; border-radius: 0.4rem;"
    >
  </a>
</figure>