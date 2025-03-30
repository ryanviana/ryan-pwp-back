import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { HydratedDocument } from 'mongoose';

export type WorkExperienceDocument = HydratedDocument<WorkExperience>;

@Schema({ timestamps: true })
export class WorkExperience {
  @Prop({ required: true })
  title: string;

  @Prop({ required: true })
  company: string;

  @Prop({ required: true })
  location: string;

  @Prop({ required: true })
  startDate: string;

  @Prop()
  endDate: string;

  @Prop({ type: [String], required: true })
  description: string[];
}

export const WorkExperienceSchema =
  SchemaFactory.createForClass(WorkExperience);
