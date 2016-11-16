odoo.define('linked_tasks.GanttView', function (require) {
    "use strict";

    var Model = require('web.Model');
    var GanttView = require('web_gantt.GanttView');

    GanttView.include({
        on_task_changed: function (task_obj) {
            var self = this;
            return this._super(task_obj).then(function (res) {
                console.log("Ma super fonction");
            });
        },
    });
});
