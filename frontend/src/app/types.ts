import { Time } from '@angular/common'

/**
 *
 * This document contains all of the types used in the frontend
 *
 */
export interface Course{

  subject: string,
  className: string,
}
export interface ScheduleWC{
  id: string,
  name: string,
  number_of_courses: string,

}
export interface UserProfile {
  userid: string,
  status: string,
  email: string,
  displayname: string,
  adminstatus: string,

}
export interface Schedule{
  name: string,
}
export interface ScheduleFull{
  schedulename: string,
  backname: string,
  status: string,
  description: string,
  courseArray: Result[]
}
export interface SchedList{
  scheduleid: number,
  schedulename: string,
  numberC: number,
  dateV: string,
  status: string,
  creatorname: string,
  description: string,
}
export interface Result{
  schedulevalueid: number,
  subjectCode: string,
  courseCode: string,
  scheduleid: number
}
export interface Scheduler{
  description: string,
  status: boolean,
  name: string,
  subjectCode: string,
  courseCode: string,

}

export interface TimeView{
  class_nbr:number,
  start_time: string,
  descrlong: string,
  end_time: string,
  facility_ID: string,
  days: string[]
  instructors: string[]
  class_section: number
  ssr_component: string,
  enrl_stat: string,
  descr: string,
}

export interface ScheduleView{
  id: number,
  subjectCode: string,
  courseCode: string,

}


export interface SearchView{
  id: number,
  subjectcode: string,
  coursecode: string,
  classname: string,
  information: TimeView[]

}

export interface Review{
  reviewid: number,
  courseid: string,
  reviewstatus: boolean,
  review: string,
  reviewer: string,
  stamp: string,
  userid: string,

}
export interface ReviewAdm{
  courseid:number
  subjectcode:string,
  coursecode:string,
  reviewid: number,

  reviewstatus: boolean,
  review: string,
  reviewer: string,
  stamp: string,
  userid: string,
}

export interface Policies{
  id: number,
  aup: string,
  privacy: string,
  dmca: string,
  workf: string,
}
export interface PolContainer{
  id: string,
  policy: string,
}
