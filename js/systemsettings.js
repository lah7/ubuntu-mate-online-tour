/*
 *  System Settings
 *  author: Anthony Dillon
 */

function SystemSettings($parent) {
  var _parent;
  var _this;
  var _date;
  var _volume;
  var _bluetooth;
  var _bluetoothVisible;
  var _onGuidedTour;
  var _systemName;
  var _mute;
  var _gotMessage;
  var _activeIcons;
  var _timeInterval;
  var _firstMinute;

  this.init = function() {
    _parent = $parent;
    _this = this;
    _date = new Date();
    _volume = 30;
    _bluetooth = true;
    _bluetoothVisible = false;
    _onGuidedTour = false;
    _systemName = 'Ubuntu Play';
    _mute = false;
    _gotMessage = false;
    _activeIcons = 9;
    _timeInterval = setInterval(function() { _this.updateClock() }, 1000);
    _firstMinute = _date.getMinutes();
    this.setClock();
    this.setSystem();
  }

  this.setSystem = function() {
    //$('#welcome #welcome-screen h1').text('Welcome to '+_systemName);
  }

  this.setGuidedTour = function($ogt) {
    _onGuidedTour = $ogt;
  }

  this.setDate= function($time) {
    _date = $time;
  }

  this.setVolume = function($volume) {
    _volume = $volume;
  }

  this.setMute = function($mute) {
    _mute = $mute;
  }

  this.setActiveIcons = function($iconCount) {
    _activeIcons = $iconCount;
  }

  this.setBluetooth = function($bluetooth) {
    _bluetooth = $bluetooth;
    if (_bluetooth) {
      $('.panel .panel-items #bluetooth ul li.bluetooth').text(_turn_on_bluetooth_);
        $('.panel .panel-items #bluetooth img').removeClass('disabled');
      $('.panel .panel-items #bluetooth ul li.BtOn').show();
    } else {
      $('.panel .panel-items #bluetooth ul li.bluetooth').text(_turn_off_bluetooth_);
      $('.panel .panel-items #bluetooth img').addClass('disabled');
      $('.panel .panel-items #bluetooth ul li.BtOn').hide();
    }
  }

  this.setBluetoothVisible = function($bluetoothVisible) {
    _bluetoothVisible = $bluetoothVisible;
  }

  this.updateTime = function() {
    _date.setMinutes( _date.getMinutes() + 1);
    this.setClock();
  }

  this.setClock = function() {
    var hours = _date.getHours();
    var minutes = _date.getMinutes();
    if (minutes < 10) { minutes = "0" + minutes; }
    if (hours < 10) { hours = "0" + hours; }
    $('#time p').text(hours + ":" + minutes + " ");
  }

  this.updateClock = function() {
    if (_firstMinute != new Date().getMinutes()) {
      clearInterval(_timeInterval);
      this.updateTime()
      setInterval(function() { _this.updateTime() }, 60000);
    }
  }

  this.onGuidedTour = function() { return _onGuidedTour; }
  this.date = function() { return _date;  }
  this.volume = function() { return _volume;  }
  this.bluetooth = function() { return _bluetooth;  }
  this.bluetoothVisible = function() { return _bluetoothVisible;  }
  this.mute = function() { return _mute;  }
  this.mail = function() { return _gotMessage; }
}
