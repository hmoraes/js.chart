from fanstatic import Library, Resource

library = Library('chart', 'resources')
chart_js = Resource(library, 'Chart.js',
                    minified='Chart.min.js')

chart_bundle_js = Resource(library, 'Chart.bundle.js',
                    minified='Chart.bundle.min.js')
