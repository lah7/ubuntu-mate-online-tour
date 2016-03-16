/*
 *  System Menu / Panels / Window Switcher
 *
 *  Authors:  2011-2014, Anthony Dillon
 *            2014, deadlight@bgr0.com
 *            ----------------------------
 *            2016, Luke Horwell <lukehorwell37+code@gmail.com>
 */

var scrollingTimer = null;
function SystemMenu($parent) {
  var _parent = $parent;
  var _this = this;
  var menuOut = false;
  var menuTimeout = null;
  var goingIn = false;
  var locked = false;
  var menuScrollAmount = 0;
  var scrolling = false;
  var selectedMenu;

  this.init = function() {
    console.log('fixme:window list unimplemented: init systemmenu')
  }

  this.handleMenuClick = function($menu) {
    var openedApp = true;
    switch($menu) {
      case 'home':
        var div = $('.folder');
        if (! div.is(':visible')) {
          if (fileSystem.isMinified()) {
            fileSystem.reset(false);
          } else {
            fileSystem.reset(true);
          }
        }
        fileSystem.open();
        $('.folder ').trigger('mousedown');
        break;
      case 'firefox':
        var div = $('.firefox-window');
        if (! div.is(':visible')) {
           _parent.firefoxSystem.open();
        }
        $('.firefox-window ').trigger('mousedown');
        break;
      case 'shotwell':
        var div = $('#shotwell');
        if (! div.is(':visible')) {
          _parent.shotwellSystem.open();
        }
        div.trigger('mousedown');
        break;
      case 'writer':
        var div = $('#libreoffice-writer-window');
        if (! div.is(':visible')) {
          _parent.libreSystem.open('writer');
        }
        div.trigger('mousedown');
        break;
      case 'impress':
        var div = $('#libreoffice-impress-window');
        if (! div.is(':visible')) {
          _parent.libreSystem.open('impress');
        }
        div.trigger('mousedown');
        break;
      case 'calc':
        var div = $('#libreoffice-calc-window');
        if (! div.is(':visible')) {
          _parent.libreSystem.open('calc');
        }
        div.trigger('mousedown');
        break;
      case 'uone':
        var div = $('#ubuntuone-window');
        if (! div.is(':visible')) {
           _parent.ubuntuOneSystem.open();
        }
        $('#ubuntuone-window ').trigger('mousedown');
        break;
      case 'software':
        var div = $('#software-centre');
        if (! div.is(':visible')) {
          _parent.softwareSystem.open();
        }
        div.trigger('mousedown');
        break;
      case 'email':
        var div = $('.email-window ');
        if (! div.is(':visible')) {
           _parent.emailSystem.open();
        }
        if (_parent.emailSystem.isWriteMinified()) {
        $('#email-write').show();
            $('#email-write ').trigger('mousedown');
          } else {
            $('.email-window ').trigger('mousedown');
          }
        break;
      case 'movieplayer':
        var div = $('#movieplayer');
        if (! div.is(':visible')) {
          moviePlayerSystem.center();
          _parent.moviePlayerSystem.open();
        }
        $('#movieplayer ').trigger('mousedown');
        break;
      case 'rubbish':
        var div = $('.folder');
        if (! div.is(':visible')) {
          if (_parent.fileSystem == null) {
            _parent.fileSystem = new FileSystem(this,'/'+_rubbish_bin_folder_);
            _parent.fileSystem.init();
          } else {
            //_parent.fileSystem.reset(! _parent.fileSystem.isMinified());
            _parent.fileSystem.updateDir('/'+_rubbish_bin_folder_);
          }
          $('.folder').show();
        } else {
          _parent.fileSystem.updateDir('/'+_rubbish_bin_folder_);
        }
        _parent.fileSystem.open();
        $('.folder ').trigger('mousedown');
        break;
      case 'workspace':
        if (_parent.workspaces.isOpen()) {
            _parent.workspaces.close();
        } else {
            _parent.workspaces.open();
        }
        break;
      default:
        openedApp = false;
        _parent.errorMessage.open();
        break;
    }
    if (openedApp) {
      console.log('fixme:handleMenuClick for openedApp.')
    }
  }

  this.getSelectedMenu = function() {
    return selectedMenu;
  }

  this.closeWindow = function($icon) {
    console.log('fixme:unimplemented closeWindow')
    _parent.guidedTourSystem.setCurrentIndex(-1);
  }

  this.openWindow = function($icon) {
    if ($("#menu ul li."+$icon).hasClass('temp')) {
      $("#menu ul li."+$icon).show();
    }
    $("#menu ul li."+$icon+" img").show();
  }

}
