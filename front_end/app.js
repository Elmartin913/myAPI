"use strict";

$(function(){
    var data = $('#title');
    var books = $.ajax({
        url: 'http://127.0.0.1:8000/person',
        data:{},
        type: 'GET',
        dataType: 'json',
        crossDomain: true,

    }).done(function(result){
        console.log('Wczytane')
        console.log(result)
        for (var i = 0; i < result.length; i++) {
            console.log(result[i].title)
            var titles = $('<p>').text(result[i].title)
            titles.attr('class')
            var div = $('<div>')
            div.attr('class')
            div.addClass('title')
            data.append(titles, div)
        }
    }).fail(function(){
        console.log('Bład wczytywania')
    }).always(function(){
        console.log('Wykonywana zawsze')
        console.log(books)
    }) // ajax

}) // f