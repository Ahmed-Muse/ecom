$(document).ready(function(){
  
    $('#div_id_line_three, #div_id_line_three_quantity, #div_id_line_three_unit_price, #div_id_line_three_total_price, #div_id_line_four, #div_id_line_four_quantity, #div_id_line_four_unit_price, #div_id_line_four_total_price, #div_id_line_five, #div_id_line_five_quantity, #div_id_line_five_unit_price, #div_id_line_five_total_price,').hide()

    $('#more-line').click(function(){
        $('#div_id_line_three, #div_id_line_three_quantity, #div_id_line_three_unit_price, #div_id_line_three_total_price').slideToggle(200)
        $('#div_id_line_four, #div_id_line_four_quantity, #div_id_line_four_unit_price, #div_id_line_four_total_price').slideToggle(200)
        $('#div_id_line_five, #div_id_line_five_quantity, #div_id_line_five_unit_price, #div_id_line_five_total_price').slideToggle(200)
        
    });
   

    
    $('#id_line_one_quantity, #id_line_one_unit_price, #id_line_two_quantity, #id_line_two_unit_price, #id_line_three_quantity, #id_line_three_unit_price, #id_line_four_quantity, #id_line_four_unit_price, #id_line_five_quantity, #id_line_five_unit_price,').keyup(function(){
        var line_one_quantity_text = $('#id_line_one_quantity').val();
        var line_one_unit_price_text = $('#id_line_one_unit_price').val();
        var line_one_total = line_one_quantity_text * line_one_unit_price_text
    
        var line_two_quantity_text = $('#id_line_two_quantity').val();
        var line_two_unit_price_text = $('#id_line_two_unit_price').val();
        var line_two_total = line_two_quantity_text * line_two_unit_price_text
    
        var line_three_quantity_text = $('#id_line_three_quantity').val();
        var line_three_unit_price_text = $('#id_line_three_unit_price').val();
        var line_three_total = line_three_quantity_text * line_three_unit_price_text
        
        var line_four_quantity_text = $('#id_line_four_quantity').val();
        var line_four_unit_price_text = $('#id_line_four_unit_price').val();
        var line_four_total = line_four_quantity_text * line_four_unit_price_text
    
        var line_five_quantity_text = $('#id_line_five_quantity').val();
        var line_five_unit_price_text = $('#id_line_five_unit_price').val();
        var line_five_total = line_five_quantity_text * line_five_unit_price_text
    
    
        var total = line_one_total + line_two_total + line_three_total + line_four_total + line_five_total
    
        $('#id_line_one_total_price').val(line_one_total);
        $('#id_line_two_total_price').val(line_two_total);
        $('#id_line_three_total_price').val(line_three_total);
        $('#id_line_four_total_price').val(line_four_total);
        $('#id_line_five_total_price').val(line_five_total);
       
        $('#id_total').val(total);
    });


      

  });

  
    function myFunction() {
        document.getElementById("demo1").innerHTML = "Hello Allifmaal!";
        
      }