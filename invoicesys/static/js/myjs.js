$(document).ready(function(){
  
    $('#div_id_line_three, #div_id_line_three_quantity, #div_id_line_three_unit_price, #div_id_line_three_total_price, #div_id_line_four, #div_id_line_four_quantity, #div_id_line_four_unit_price, #div_id_line_four_total_price, #div_id_line_five, #div_id_line_five_quantity, #div_id_line_five_unit_price, #div_id_line_five_total_price,').hide()

    $('#more-line').click(function(){
        $('#div_id_line_three, #div_id_line_three_quantity, #div_id_line_three_unit_price, #div_id_line_three_total_price').slideToggle(200)
        $('#div_id_line_four, #div_id_line_four_quantity, #div_id_line_four_unit_price, #div_id_line_four_total_price').slideToggle(200)
        $('#div_id_line_five, #div_id_line_five_quantity, #div_id_line_five_unit_price, #div_id_line_five_total_price').slideToggle(200)
        
    });
   
   
  });