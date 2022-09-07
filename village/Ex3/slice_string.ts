
import {fs} from 'fs';
import {parser} from 'csv-parser';

function slice_string(s: string, start1: number, end1: number, start2: number, end2: number): string {
    return s.slice(start1, end1+1) + " " + s.slice(start2, end2+1);
}