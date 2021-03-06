
    $(document).ready(function()
    {
        $('#examplePalette').palette({
            length: 4,
            onSelect: function() {
                var col =( $(this).find('.coloring').attr('title') ); 
                console.log(col);
                document.body.style.setProperty("--color-primary-color", col);
            }
        });
    });

(function($){
    /*
    * palette.js - rev 1
    * Copyright (c) 2012, ToxicWar
    * Liscensed under the MIT License (MIT-LICENSE.txt)
    * http://www.opensource.org/licenses/mit-license.php
    */

    /*
    * Created a palette around a textfield
    *
    * @param    object  opt     options
    */
    jQuery.fn.palette = function(opt){

        options = jQuery.extend(
            {
                // array colors
                colors: [  '#ff2e2b' , '#aa4652','#8B008B', '#FF1493', '#2196F3', '#8FD8D8' , '#ADFF2F', '#008000', '#90EE90', '#10EA90'],
                // palette length
                length: 8,
                onSelect: function() {}

            }, opt);

        return this.each(function() {
            var $self = $(this).wrap('<span class="palettebox"></span>').parent('.palettebox');

            $self.click(function(e) {
                var $clicked = $(e.target);
                if ( $clicked.hasClass('palette') ) {
                    $self.uncolor();
                    $clicked.html('').addClass('coloring');
                };

                options.onSelect.call($self);
            });

            var count = 0;
            for ( i=0; i<options.colors.length; i++ ) {
                count++;

                $('<span class="palette" title="' + options.colors[i] + '"></span>')
                    .appendTo( $self )
                    .css( 'background-color', options.colors[i] );
            };
        });
    };

    /*
    * Unselect the selected palette
    *
    * @param	boolean	clearTextfield	option to clear the textfield as well
    * @return	object	each item passed in
    */
    jQuery.fn.uncolor = function(clearTextfield) {
        return this.each(function() {
            $('.coloring', this).html('').removeClass('coloring');
        });
    };

    /*
    * Add palette
    *
    * @param    color
    */
    jQuery.fn.addPalette = function(color) {
        return this.each(function() {
            var $self = $(this).parent('.palettebox');

            $('<span class="palette" title="' + color + '"></span>')
                .appendTo( $self )
                .css( 'background-color', color );
            if (options.colors.length % options.length === 0 )
                $('.palettebox').append('<br class="clear"/>');
        });
    };

    /*
     * Add color
     *
     * @param   color
     */
    jQuery.fn.addColor = function(color) {
        options.colors.push(color);
        $("#examplePalette").addPalette(color);
    };

    /*
     *  Change color
     *
     *  @param  color
     */
    jQuery.fn.changeColor = function(color) {
        $(".coloring").css('background-color', color);
    };
})(jQuery);