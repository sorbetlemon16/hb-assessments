"use strict";

$('#get-human').on('submit', (evt) => {
  evt.preventDefault();

  const selectedId = $('#human-id').val();

  $.get(`/api/human/${selectedId}`, (res) => {
    $('#fname').html(res.fname);
    $('#lname').html(res.lname);
    $('#email').html(res.email);
  });
});


// Alternative solution
//
// document.querySelector('#get-human')
//   .addEventListener('submit', (evt) => {
//     evt.preventDefault();
//
//     const selectedId = document.querySelector('#human-id').value;
//     // or:
//     // const selectedId = evt.target.elements['human_id']value;
//
//     $.get(`/api/human/${selectedId}`, (res) => {
//       document.querySelector('#fname').innerHTML = res.fname;
//       document.querySelector('#lname').innerHTML = res.lname;
//       document.querySelector('#email').innerHTML = res.email;
//     });
//   });
