# -*- coding: utf-8 -*-
__version__ = '1.2.8.post1'

import warnings

warnings.warn(
    "This package is deprecated. All code has been merged into the original package django-background-tasks.",
    DeprecationWarning,
    stacklevel=2
)

default_app_config = 'background_task.apps.BackgroundTasksAppConfig'


def background(*arg, **kw):
    from background_task.tasks import tasks
    return tasks.background(*arg, **kw)
