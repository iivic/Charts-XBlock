/* Javascript for ChartsXBlock. */
function ChartsXBlockStudio(runtime, element, data) {

    function dataSaved() {
        window.location.reload(false);
    }

    $('.save-button', element).click(function (eventObject) {
        var handlerUrl = runtime.handlerUrl(element, 'save_data'),
            displayName = $('#display_name').val(),
            data = {
                display_name: displayName
            };

        $.ajax({
            type: "POST",
            url: handlerUrl,
            data: JSON.stringify({"data": "world"}),
            success: dataSaved
        });
    });

    $('.cancel-button', element).click(function (eventObject) {
        runtime.notify('cancel', {});
    });

    $(function ($) {
        /* Here's where you'd do things on page load. */

        var list = '<li class="has-submenu"><a>Chart type</a><ul>';
        $.each(data.jsonData, addData);

        function addData(key, val) {
            if (val instanceof Object) {
                list += '<li class="has-submenu">' +
                        '<a>' + key + '</a>' +
                        '<ul>';
                $.each(val, addData);
                list += '</ul><span class="sub-toggle"><i>▼</i></span></li>';
            } else {
                list += '<li class="has-submenu">' +
                        '<a>' + key + '</a>' +
                        '<ul>' +
                        '<li><a>' + val + '</a></li>' +
                        '</ul><span class="sub-toggle"><i>▼</i></span></li>';
            }
        }

        list += '</ul><span class="sub-toggle"><i>▼</i></span></li>';
        $("#navigation").html(list);

        $('#navigation').slimmenu(
            {
                animSpeed: 'medium',
                easingEffect: null
            }
        );
    });
}
