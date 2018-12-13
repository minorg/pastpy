$().ready(function () {
    var loadedIndex = lunr.Index.load(index);

    var urlParameters = {};
    {
        var match,
            pl = /\+/g, // Regex for replacing addition symbol with a space
            search = /([^&=]+)=?([^&]*)/g,
            decode = function (s) {
                return decodeURIComponent(s.replace(pl, " "));
            },
            query = window.location.search.substring(1);

        while (match = search.exec(query)) {
            urlParameters[decode(match[1])] = decode(match[2]);
        }
    }

    var q = urlParameters["q"];
    if (!q) {
        q = "";
    }
    $(".search-input").val(q);
    $(".search-term").html(q);

    var searchResults = loadedIndex.search(q);

    var searchResultTemplate = $("#object-card-html-mustache").html();

    var searchResultsHtml = "";
    for (var searchResultI = 0; searchResultI < searchResults.length; searchResultI++) {
        var searchResult = searchResults[searchResultI];
        var object_ = {};
        Object.assign(object_, objects[searchResult.ref]);
        object_["root_relative_href"] = ".";
        searchResultsHtml += Mustache.render(searchResultTemplate, object_);
    }

    $("#search-results").html(searchResultsHtml);
});