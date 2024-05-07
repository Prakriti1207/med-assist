$(document).ready(function() {
  
    $.getJSON('http://localhost:8000/fetch_all_category_json', function (data) {

        var records = data.data
        records.map((item) => {

            $('#categoryid').append($('<option>').text(item.categoryname).val(item.categoryid))
        })
        $('#categoryid').formSelect()  // to refresh the dropdown
    })

    $('#categoryid').change(function () {
     
        $('#subcategoryid').empty()
        $('#subcategoryid').append($('<option disabled selected>').text('Choose your Sub Category'))
       
        $.getJSON('http://localhost:8000/fetch_all_subcategory_json', {categoryid: $('#categoryid').val()}, function (data) {

         
            var records = data.data
            // console.log(record)
            records.map((item) => {

                $('#subcategoryid').append($('<option>').text(item.subcategoryname).val(item.subcategoryid))
            })
            $('#subcategoryid').formSelect()
        })
        
    })
   

    $('#subcategoryid').change(function () {
        
        $('#brandid').empty()
        $('#brandid').append($('<option disabled selected>').text('Choose your brand'))
      
        $.getJSON('http://localhost:8000/fetch_all_brand_json', {subcategoryid: $('#subcategoryid').val()}, function (data) {
            var records = data.data
            // alert(JSON.stringify(records))
            records.map((item) => {

                $('#brandid').append($('<option>').text(item.brandname).val(item.brandid))

            })
            $('#brandid').formSelect()
        })

    })
})


