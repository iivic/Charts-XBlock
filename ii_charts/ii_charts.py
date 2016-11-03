"""TO-DO: Write a description of what this XBlock is."""
import json
import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment
from django.template import Context, Template


class ChartsXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    # Fields are defined on the class.  You can access them in your code as
    # self.<fieldname>.

    chart_type = String(
        default="Bar Chart",
        scope=Scope.settings
    )

    display_name = String(
        display_name="Display Name",
        default="Charts-XBlock",
        scope=Scope.settings
    )

    json_data = json.loads("""{
        "comparison": {
            "among items": {
                "One variable per item": {
                    "Few Categories": {
                        "Many Items": "Bar Chart",
                        "Few Items": "Column Chart"
                    },
                    "Many Categories": "Table or Table with Embedded Chart"
                },
                "Two variables per item": "Variable Width Column Chart"
            },
            "over time": {
                "Many Periods": {
                    "Cyclic Data": "Circular Area Chart",
                    "Non-Cyclical Data": "Line Chart"
                },
                "Few Periods": {
                    "Single or Few Categories": "Column Chart",
                    "Many Categories": "Line Chart"
                }
            }
        },
        "composition": {
            "Changing Over Time": {
                "Few Periods": {
                    "Only Relative Differences Matter": "Stacked 100% Column Chart",
                    "Relative and Absolute Differences Matter": "Stacked Column Chart"
                },
                "Many Periods": {
                    "Only Relative Differences Matter": "Stacked 100% Area Chart",
                    "Relative and Absolute Differences Matter": "Stacked Area Chart"
                }
            },
            "Static": {
                "Simple Share of Total": "Pie Chart",
                "Accumulation or Subtraction to Total": "Waterfall Chart",
                "Components of Components": "Stacked 100% Column Chart with Subcomponents"
            }
        },
        "distribution": {
            "Single variable": {
                "Few data points": "Column Histogram",
                "Many data points": "Line Histogram"
            },
            "Two variables": "Scatter Chart",
            "Three variables": "3D Area Chart"
        },
        "relationship": {
            "two variables": "Scatter Chart",
            "three variables": "Bubble Chart"
        }
    }""")

    @staticmethod
    def resource_string(path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def save_data(self, data):
        """Saves data."""
        self.display_name = data.get('display_name')
        return

    def student_view(self, context=None):
        """
        The primary view of the ChartsXBlock, shown to students
        when viewing courses.
        """
        frag = Fragment(Template(self.resource_string("public/html/ii_charts.html")).render(
            Context({'self': self})))
        frag.add_css(self.resource_string("public/css/ii_charts.css"))
        frag.add_javascript(self.resource_string("public/js/src/ii_charts.js"))
        frag.initialize_js('ChartsXBlock', {'displayName': self.display_name})
        return frag

    def studio_view(self, context):
        """
        Editing view in Studio
        """
        frag = Fragment(Template(self.resource_string("public/html/ii_charts-studio.html")).render(
            Context({'self': self})))
        frag.add_css(self.resource_string("public/css/slimmenu.min.css"))
        frag.add_css(self.resource_string("public/css/ii_charts.css"))
        frag.add_javascript(self.resource_string("public/js/src/jquery.slimmenu.min.js"))
        frag.add_javascript(self.resource_string("public/js/src/ii_charts-studio.js"))
        frag.initialize_js('ChartsXBlockStudio', {'jsonData': self.json_data})
        return frag


# TO-DO: change this to create the scenarios you'd like to see in the
# workbench while developing your XBlock.
@staticmethod
def workbench_scenarios():
    """A canned scenario for display in the workbench."""
    return [
        ("ChartsXBlock",
         """<ii_charts/>
         """),
        ("Multiple ChartsXBlock",
         """<vertical_demo>
            <ii_charts/>
            <ii_charts/>
            <ii_charts/>
            </vertical_demo>
         """),
    ]
