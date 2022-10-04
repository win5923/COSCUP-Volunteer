''' Projects '''
from typing import Any

import arrow
from fastapi import APIRouter, Depends, HTTPException, Path, status

from api.apistructs.items import ProjectItem, TeamItem
from api.apistructs.projects import (ProjectAllOut, ProjectItemUpdateInput,
                                     ProjectItemUpdateOutput,
                                     ProjectTeamsOutput)
from api.dependencies import get_current_user
from module.project import Project
from module.team import Team

router = APIRouter(
    prefix='/projects',
    tags=['projects'],
    responses={status.HTTP_404_NOT_FOUND: {'description': 'Not found'}},
)


@router.get('',
            summary='List all projects.',
            response_model=ProjectAllOut,
            responses={
                status.HTTP_404_NOT_FOUND: {'description': 'Project not found'}},
            response_model_exclude_none=True,
            )
async def projects_all(current_user: dict[str, Any] = Depends(get_current_user)) -> ProjectAllOut:
    ''' List all projects '''
    datas = []
    for data in Project.all():
        if 'owners' in data and current_user['uid'] in data['owners']:
            data['id'] = data['_id']
            datas.append(ProjectItem.parse_obj(data))
        else:
            datas.append(
                ProjectItem.parse_obj({
                    'id': data['_id'],
                    'name': data['name'],
                    'desc': data['desc'],
                }))

    return ProjectAllOut(datas=datas)


@router.patch('/{pid}',
              summary='Update one project info. *owners',
              tags=['owners', ],
              response_model=ProjectItemUpdateOutput,
              responses={
                  status.HTTP_404_NOT_FOUND: {'description': 'Project not found'},
                  status.HTTP_401_UNAUTHORIZED: {'description': '`owners` permission required'},
              },
              response_model_exclude_none=True,
              )
async def projects_one_update(
        update_data: ProjectItemUpdateInput,
        pid: str = Path(..., description='project id'),
        current_user: dict[str, Any] = Depends(get_current_user),
) -> ProjectItemUpdateOutput | None:
    ''' Update one project info

    Permissions
    -----------
    - **owners**

    '''

    project = Project.get(pid=pid)
    if not project:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    if 'owners' not in project or current_user['uid'] not in project['owners']:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    data = update_data.dict(exclude_none=True)
    if 'action_date' in data:
        data['action_date'] = arrow.get(data['action_date']).int_timestamp

    Project.update(pid=pid, data=data)

    return ProjectItemUpdateOutput.parse_obj(data)


@router.get('/{pid}/teams',
            summary='Lists of teams in project.',
            response_model=ProjectTeamsOutput,
            responses={
                status.HTTP_404_NOT_FOUND: {'description': 'Project not found'}},
            response_model_exclude_none=True,
            )
async def projects_teams(
        pid: str = Path(..., description='project id'),
        current_user: dict[str, Any] = Depends(  # pylint: disable=unused-argument
            get_current_user),
) -> ProjectTeamsOutput | None:
    ''' Lists of teams in project '''
    teams = []
    for team in Team.list_by_pid(pid=pid):
        teams.append(TeamItem.parse_obj(team))

    return ProjectTeamsOutput.parse_obj({'teams': teams})