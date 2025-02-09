function navigateTo(page) {
    fetch(`/page/${page}`)
        .then(response => {
            if (!response.ok) {
                throw new Error('Page not found');
            }
            return response.text();
        })
        .then(html => {
            document.getElementById('app').innerHTML = html;
            updateActiveMenu(page);

            // Load the script only if the graph page is loaded
            if (page === 'graph') {
                loadScriptsForGraphPage();
            }
            if (page === 'index') {
                loadScriptsForIndexPage();
            }
        })
        .catch(error => {
            console.error('Error loading page:', error);
            document.getElementById('app').innerHTML = '<h1>Error: Page not found</h1>';
        });

}

// Search Users Function (Handles SPA Search Without Reload)
function searchUsers(event) {
    if (event) event.preventDefault(); // Prevent form from reloading the page

    let searchQuery = document.getElementById("search-input").value;
    console.log(searchQuery)
    fetch(`/admin/search_users?search=${searchQuery}`)

        .then(response => response.text())
        .then(html => {

            document.getElementById('user_list').innerHTML = html;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('user_list').innerHTML = "<h1>Error loading users</h1>";
        });
}

function loadScriptsForGraphPage() {
    // List of scripts to load for the graph page
    const scripts = [
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js",
        "https://d3js.org/d3.v7.min.js",
        "/static/JS/graph.js"
    ];

    // Function to load a single script
    function loadScript(src) {
        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = src;
            script.onload = resolve;
            script.onerror = reject;
            document.body.appendChild(script);
        });
    }

    // Load all scripts sequentially
    scripts.reduce((promise, src) => {
        return promise.then(() => loadScript(src));
    }, Promise.resolve())
        .then(() => {
            console.log('All scripts for the graph page have been loaded.');
        })
        .catch(error => {
            console.error('Error loading scripts:', error);
        });
}
function loadScriptsForIndexPage() {
    // List of scripts to load for the graph page
    const scripts = [
        "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js",
        "https://d3js.org/d3.v7.min.js",
        "/static/JS/market.js",
        "https://cdn.jsdelivr.net/npm/chart.js",
        "https://cdn.socket.io/4.5.1/socket.io.min.js"
    ];

    // Function to load a single script
    function loadScript(src) {
        return new Promise((resolve, reject) => {
            const script = document.createElement('script');
            script.src = src;
            script.onload = resolve;
            script.onerror = reject;
            document.body.appendChild(script);
        });
    }

    // Load all scripts sequentially
    scripts.reduce((promise, src) => {
        return promise.then(() => loadScript(src));
    }, Promise.resolve())
        .then(() => {
            console.log('All scripts for the graph page have been loaded.');
        })
        .catch(error => {
            console.error('Error loading scripts:', error);
        });
}

function updateActiveMenu(activePage) {
    // Remove 'current-page' and 'active' from all menu items
    document.querySelectorAll('li').forEach(item => {
        item.classList.remove('current-page', 'active');
    });

    // Find the clicked menu item
    document.querySelectorAll('a').forEach(link => {
        if (link.getAttribute('onclick') === `navigateTo('${activePage}')`) {
            let listItem = link.parentElement;
            listItem.classList.add('current-page', 'active',);


            // If it's inside a nested menu, activate its parent "treeview"
            let parentTreeView = listItem.closest('.treeview');
            if (parentTreeView) {
                parentTreeView.classList.add('current-page', 'active');

            }
        }
    });
}

// Load the default page on initial load
document.addEventListener('DOMContentLoaded', () => {
    navigateTo('home');
});

// Sidebar Menu on dropdown
$.sidebarMenu = function (menu) {
    var animationSpeed = 300;

    // Click event for .treeview parent items (expand/collapse)
    $(menu).on("click", "li.treeview > a", function (e) {
        var $this = $(this);
        var checkElement = $this.next(".treeview-menu");

        // If the menu is already open, close it
        if (checkElement.is(":visible")) {
            checkElement.slideUp(animationSpeed, function () {
                checkElement.removeClass("menu-open");
            });
            $this.parent("li").removeClass("active");
        } else {
            // Close all other treeview-menu items
            var $otherMenus = $(menu).find(".treeview-menu:visible").not(checkElement);
            $otherMenus.slideUp(animationSpeed, function () {
                $(this).removeClass("menu-open");
            });

            // Remove 'active' class from all other treeview items
            $(menu).find("li.treeview").not($this.parent("li")).removeClass("active");

            // Open the clicked treeview menu and add the menu-open class
            checkElement.slideDown(animationSpeed, function () {
                checkElement.addClass("menu-open");
                $this.parent("li").addClass("active");
            });
        }

        e.preventDefault();
    });

    // Click event for non-treeview (normal) menu items
    $(menu).on("click", "li:not(.treeview) > a", function (e) {
        // Only collapse menus if this is a top-level non-treeview item
        if (!$(this).closest('.treeview-menu').length) {
            $(menu).find(".treeview-menu:visible").slideUp(animationSpeed, function () {
                $(this).removeClass("menu-open");
            });
            $(menu).find("li.treeview").removeClass("active");
        }
    });

    // Handle clicks on nested menu items
    $(menu).on("click", ".treeview-menu li a", function (e) {
        // Remove active class from all items at the same level
        $(this).closest('ul').find('li').removeClass('active');
        // Add active class to the clicked item's parent li
        $(this).parent('li').addClass('active');
        // Keep parent treeview active
        $(this).closest('.treeview').addClass('active');
        // Keep menu open
        $(this).closest('.treeview-menu').addClass('menu-open').show();
        // Don't stop propagation - let the click bubble up to handle navigation
    });
};

// Initialize the sidebar menu
$.sidebarMenu($(".sidebar-menu"));

// Custom Sidebar JS
jQuery(function ($) {
    //toggle sidebar
    $("#toggle-sidebar").on("click", function () {
        $(".page-wrapper").toggleClass("toggled");
    });

    // Pin sidebar on click
    $("#pin-sidebar").on("click", function () {
        if ($(".page-wrapper").hasClass("pinned")) {
            // unpin sidebar when hovered
            $(".page-wrapper").removeClass("pinned");
            $("#sidebar").unbind("hover");
        } else {
            $(".page-wrapper").addClass("pinned");
            $("#sidebar").hover(
                function () {
                    console.log("mouseenter");
                    $(".page-wrapper").addClass("sidebar-hovered");
                },
                function () {
                    console.log("mouseout");
                    $(".page-wrapper").removeClass("sidebar-hovered");
                }
            );
        }
    });

    // Pinned sidebar
    $(function () {
        $(".page-wrapper").hasClass("pinned");
        $("#sidebar").hover(
            function () {
                console.log("mouseenter");
                $(".page-wrapper").addClass("sidebar-hovered");
            },
            function () {
                console.log("mouseout");
                $(".page-wrapper").removeClass("sidebar-hovered");
            }
        );
    });

    // Toggle sidebar overlay
    $("#overlay").on("click", function () {
        $(".page-wrapper").toggleClass("toggled");
    });

    // Added by Srinu
    $(function () {
        // When the window is resized,
        $(window).resize(function () {
            // When the width and height meet your specific requirements or lower
            if ($(window).width() <= 768) {
                $(".page-wrapper").removeClass("pinned");
            }
        });
        // When the window is resized,
        $(window).resize(function () {
            // When the width and height meet your specific requirements or lower
            if ($(window).width() >= 768) {
                $(".page-wrapper").removeClass("toggled");
            }
        });
    });
});

//Modal 
document.addEventListener("DOMContentLoaded", function () {
    // Select the flash message element
    var flashMessageElement = document.getElementById('flashModal');

    // Show the flash message and set a timer to hide it after 3 seconds
    setTimeout(function () {
        // Fade out the alert and remove it from the DOM after 3 seconds
        flashMessageElement.classList.add('fade');
    }, 3000); // 3 second timer
    setTimeout(function () {
        // Fade out the alert and remove it from the DOM after 3 seconds
        flashMessageElement.remove();
    }, 3200); // 3 second timer

});
/***********
***********
***********
    Bootstrap JS 
***********
***********
***********/

// Tooltip
var tooltipTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="tooltip"]')
);
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
});

// Popover
var popoverTriggerList = [].slice.call(
    document.querySelectorAll('[data-bs-toggle="popover"]')
);
var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
    return new bootstrap.Popover(popoverTriggerEl);
});
