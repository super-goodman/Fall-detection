format 224

classcanvas 128023 class_ref 128023 // FallThread
  classdiagramsettings member_max_width 0 end
  xyzwh 310 170 2000 145 113
end
classcanvas 128151 class_ref 128151 // ICM20948
  classdiagramsettings member_max_width 0 end
  xyz 550 149 2000
end
classcanvas 128279 class_ref 128279 // LEDMatrix
  classdiagramsettings member_max_width 0 end
  xyz 60 525 2000
end
classcanvas 128407 class_ref 128407 // LEDThread
  classdiagramsettings member_max_width 0 end
  xyz 303 504 2000
end
classcanvas 128535 class_ref 128535 // LPS22HB
  classdiagramsettings member_max_width 0 end
  xyz 549 513 2000
end
classcanvas 128663 class_ref 128663 // SHTC3
  classdiagramsettings member_max_width 0 end
  xyz 313 330 2000
end
classcanvas 128791 class_ref 128791 // DataAnalysis
  classdiagramsettings member_max_width 0 end
  xyz 27 174 2000
end
classcanvas 128919 class_ref 128919 // DataBaseManager
  classdiagramsettings member_max_width 0 end
  xyz 287 28 2000
end
relationcanvas 130455 relation_ref 128535 // getData
  from ref 128407 z 2001 label "getData" italic max_width 255 xyz 478 543 3000 to ref 128535
  no_role_a no_role_b
  multiplicity_a_pos 531 571 3000 multiplicity_b_pos 465 571 3000
end
relationcanvas 130583 relation_ref 128663 // getData
  from ref 128407 z 2001 label "getData" italic max_width 255 xyz 391.5 466.5 3000 to ref 128663
  no_role_a no_role_b
  multiplicity_a_pos 362 456 3000 multiplicity_b_pos 362 482 3000
end
relationcanvas 130711 relation_ref 128791 // display
  from ref 128407 z 2001 label "display" italic max_width 255 xyz 246 542 3000 to ref 128279
  no_role_a no_role_b
  multiplicity_a_pos 236 571 3000 multiplicity_b_pos 285 571 3000
end
relationcanvas 131351 relation_ref 129303 // sendDataBase
  from ref 128023 z 2001 label "sendDataBase" italic max_width 255 xyz 390.5 127.5 3000 to ref 128919
  no_role_a no_role_b
  multiplicity_a_pos 365 106 3000 multiplicity_b_pos 365 148 3000
end
relationcanvas 131479 relation_ref 129431 // Analysis
  decenter_begin 476
  from ref 128023 z 2001 label "Analysis" italic max_width 255 xyz 244 207.5 3000 to ref 128791
  no_role_a no_role_b
  multiplicity_a_pos 239 232 3000 multiplicity_b_pos 292 231 3000
end
relationcanvas 131607 relation_ref 129559 // getData
  from ref 128023 z 2001 label "getData" italic max_width 255 xyz 479 209.5 3000 to ref 128151
  no_role_a no_role_b
  multiplicity_a_pos 532 234 3000 multiplicity_b_pos 464 234 3000
end
end
