var calendar = new tui.Calendar(document.getElementById('calendar'), {
    defaultView: 'month',
    taskView: true,    // can be also ['milestone', 'task']
    scheduleView: true,  // can be also ['allday', 'time']
    useCreationPopup: true,
    useDetailPopup: true,
    template: {
        milestone: function(schedule) {
            return '<span style="color:red;"><i class="fa fa-flag"></i> ' + schedule.title + '</span>';
        },
        milestoneTitle: function() {
            return 'Milestone';
        },
        task: function(schedule) {
            return '&nbsp;&nbsp;#' + schedule.title;
        },
        taskTitle: function() {
            return '<label><input type="checkbox" />Task</label>';
        },
        allday: function(schedule) {
            return schedule.title + ' <i class="fa fa-refresh"></i>';
        },
        alldayTitle: function() {
            return 'All Day';
        },
        time: function(schedule) {
            return schedule.title + ' <i class="fa fa-refresh"></i>' + schedule.start;
        }
    },
    month: {
        daynames: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        startDayOfWeek: 0,
        narrowWeekend: true
    },
    week: {
        daynames: ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'],
        startDayOfWeek: 0,
        narrowWeekend: true
    }
});

calendar.createSchedules([
    {
        id: '1',
        calendarId: '1',
        title: 'my schedule',
        category: 'time',
        dueDateClass: '',
        start: '2019-02-18T22:30:00+09:00',
        end: '2019-02-19T02:30:00+09:00'
    },
    {
        id: '2',
        calendarId: '1',
        title: 'second schedule',
        category: 'time',
        dueDateClass: '',
        start: '2019-02-18T17:30:00+09:00',
        end: '2019-02-19T17:31:00+09:00',
        isReadOnly: true    // schedule is read-only
    }
]);

// calendar.on('clickSchedule', function(event) {
//     var schedule = event.schedule;

//     if (lastClickSchedule) {
//         calendar.updateSchedule(lastClickSchedule.id, lastClickSchedule.calendarId, {
//             isFocused: false
//         });
//     }
//     calendar.updateSchedule(schedule.id, schedule.calendarId, {
//         isFocused: true
//     });

//     lastClickSchedule = schedule;
//     // open detail view
// });

calendar.on('beforeCreateSchedule', function(event) {
    var startTime = event.start;
    var endTime = event.end;
    var isAllDay = event.isAllDay;
    var guide = event.guide;
    var triggerEventName = event.triggerEventName;
    var schedule;
    calendar.openCreationPopup(event);
    if (triggerEventName === 'click') {
        // open writing simple schedule popup
        // schedule = openCreationPopup(event);
    } else if (triggerEventName === 'dblclick') {
        // open writing detail schedule popup
        // schedule = openCreationPopup(event);
    }

    // calendar.createSchedules([schedule]);
});